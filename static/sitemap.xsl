<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="html" indent="yes"/>
  <xsl:template match="/">
    <html>
      <head>
        <title>Sitemap for Kashi Ganga Aarti</title>
        <style>
          body { font-family: Arial, sans-serif; background: #f9f9f9; color: #222; }
          h1 { color: #b8860b; }
          table { border-collapse: collapse; width: 100%; background: #fff; }
          th, td { border: 1px solid #ddd; padding: 8px; }
          th { background: #f3e9c7; color: #222; }
          tr:nth-child(even) { background: #f7f7f7; }
        </style>
      </head>
      <body>
        <h1>Sitemap for Kashi Ganga Aarti</h1>
        <table>
          <tr>
            <th>URL</th>
            <th>Change Frequency</th>
            <th>Priority</th>
          </tr>
          <xsl:for-each select="urlset/url">
            <tr>
              <td><a href="{loc}"><xsl:value-of select="loc"/></a></td>
              <td><xsl:value-of select="changefreq"/></td>
              <td><xsl:value-of select="priority"/></td>
            </tr>
          </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
