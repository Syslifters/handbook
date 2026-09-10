---
url: 'https://handbook.syslifters.com/de/datensicherheit.md'
description: >-
  Wie wir Kundendaten behandeln und während Pentests Evidenzen, Notizen und
  Berichte schützen.
---

# Datensicherheit

Wir verwalten unsere Notizen und Berichte in der von uns selbst entwickelten Pentest-Reporting-Lösung SysReptor (welche wir international an Pentesting-Teams vertreiben; source-available auf [GitHub](https://github.com/syslifters/sysreptor/)). Die Berechtigungsvergabe auf Projekte erfolgt stets nach dem Need-to-know-Prinzip. Gespeicherte Daten wie Bilder, Evidenzen, Datenbank-Einträge – sind serverseitig verschlüsselt (Encrypted Data at Rest; siehe auch [Dokumentation von SysReptor](https://docs.sysreptor.com/setup/configuration/#data-encryption-at-rest)) und die Übermittlung (Data in Transit) erfolgt ebenso verschlüsselt (mittels TLS/HTTPS).

Drei Monate nachdem ein (Re-)Test abgeschlossen wurde, werden die Berichte, Notizen und Evidenzen verschlüsselt und können nur mittels Hardware-Tokens und eines Vier-Augen-Prinzips wiederhergestellt werden (Verschlüsselung mittels Shamir-Secret-Sharing-Algorithmus; weitere Informationen: <https://docs.sysreptor.com/insights/archiving/>), bis sie nach Ablauf unserer Aufbewahrungsfristen automatisch gelöscht werden.

Die Kommunikation zwischen Komponenten unserer internen Netzwerke erfolgt Ende-zu-Ende-verschlüsselt (mithilfe eines Tailscale-VPNs; teils mit mehreren Verschlüsselungs-Layern).

Wir stellen jedem Pentester ein Smartphone mit eigener Dienstnummer und einen Computer zur Verfügung. Die Privatnutzung ist aus Sicherheits- und Datenschutzgründen untersagt. Mitglieder von Projektteams kommunizieren mit dem Signal-Messenger und verschwindenden Nachrichten. Computer schützen wir mit IKARUS / HarfangLab (Endpunktschutz, Erkennung und Vulnerability Management).

Alle Web-Pentest-Aktivitäten werden über lokale Proxyserver der Pentester ([PortSwigger Burp](https://portswigger.net/burp)) protokolliert und drei Monate nach Abschluss der Pentests bzw. der Retests gelöscht.

Zudem verfügen wir über Vertraulichkeitsvereinbarungen mit unseren Mitarbeitern.
