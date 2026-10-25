#!/usr/bin/env python3
import sys, struct, zlib, io

PNG_SIG = b"\x89PNG\r\n\x1a\n"

def read_chunks(b):
    assert b.startswith(PNG_SIG), "Not a PNG"
    i = len(PNG_SIG)
    while True:
        L = int.from_bytes(b[i:i+4],"big")
        ctype = b[i+4:i+8]
        data = b[i+8:i+8+L]
        crc  = b[i+8+L:i+12+L]
        yield (ctype, data, crc)
        i += 12 + L
        if ctype == b"IEND": break

def parse_itxt(data):
    parts = data.split(b"\x00", 3)
    if len(parts) < 4: return None, None
    key = parts[0].decode("latin-1", "ignore")
    comp_flag = parts[1][:1]
    rest = parts[2] + b"\x00" + parts[3]
    lang_end = rest.find(b"\x00")
    if lang_end == -1: return key, None
    rest2 = rest[lang_end+1:]
    trans_end = rest2.find(b"\x00")
    if trans_end == -1: return key, None
    text = rest2[trans_end+1:]
    if comp_flag == b"\x01":
        try: text = zlib.decompress(text)
        except zlib.error: pass
    return key, text

def build_itxt(keyword, xml_bytes, compress=False):
    key = keyword.encode("latin-1") + b"\x00"
    comp_flag = b"\x01" if compress else b"\x00"
    comp_method = b"\x00"
    language = b"\x00"
    translated = b"\x00"
    payload = zlib.compress(xml_bytes) if compress else xml_bytes
    data = key + comp_flag + comp_method + language + translated + payload
    ctype = b"iTXt"
    length = len(data).to_bytes(4,"big")
    crc = (zlib.crc32(ctype + data) & 0xffffffff).to_bytes(4,"big")
    return length + ctype + data + crc

def main(inp, xmpfile, outp):
    xml = open(xmpfile, "rb").read()
    b = open(inp, "rb").read()
    out = io.BytesIO(); out.write(PNG_SIG)
    for ctype, data, crc in read_chunks(b):
        if ctype == b"IEND":
            out.write(build_itxt("XML:com.adobe.xmp", xml, compress=False))
            out.write((0).to_bytes(4,"big") + b"IEND" + crc)
        else:
            if ctype == b"iTXt":
                key, _ = parse_itxt(data)
                if key == "XML:com.adobe.xmp":
                    continue
            out.write(len(data).to_bytes(4,"big") + ctype + data + crc)
    open(outp, "wb").write(out.getvalue())

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: inject_xmp.py input.png my.xmp output.png")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2], sys.argv[3])

