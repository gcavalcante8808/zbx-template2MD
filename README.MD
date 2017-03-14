zbx-template2MD
---------------

This is a simple project to help teams that work with Zabbix to visualize their template's information in a markup format, Markdown in this case.

You can use some online tools like http://dillinger.io/ to view MD files if needed.


How to Install
--------------

You can grab the binary directly from the releases page. After the download, mark it as executable and run it from the folder where the "zbx_export_templates.xml" files resides. Something like the following should work:

```
    wget https://github.com/gcavalcante8808/zbx-template2MD/releases/download/latest/template2MD
    chmod +x template2MD
    ./template2MD
```

After the proccess, check the file "zbx_templates.md".

How It Works
------------

The Binary "template2MD" takes a file named "zbx_export_templates.xml" and create an Markdown file containing Template and Items information in a readable format. The file resides in the same
folder of the binary and is called "zbx_templates.md".

Caveats
-------

Some strings that come from zabbix in odd formats (like "ISO8859-2" and so on) sometimes cannot be translated; when this occurs a warning will be printed into the terminal.


How to Generate the Binary
--------------------------

If you don't want to use our releases, you'll need to install the following requirements (as needed by pyinstaller):

 * ucl-upx.
 * binutils. 
 * requirements.txt (pip)

Then, generate the api file based on the xsd and the binary with the following commands:

```
    generateDS.py -o template_api.py -s templatesubs.py zabbix-schema.xsd
    pyinstaller -F template2MD.py
```

The binary will be created in the folder "dist" with the name "template2MD".
