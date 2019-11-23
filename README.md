# Unofficial DeepL Translator

py-deepl is a free python library that translates text using the DeepL translating service without the need for API authentication.

Please consider using the official API for bulk requests.

### Installation

Before using the library, you must install the `requests-html` package.

```pip install requests-html```

To install, you only need to import deepl.py.

```import deepl```

Note that when you use the library for the first time, `requests-html` will perform a one time download for Chromium Puppeteer.

### Basic Usage

```python
import deepl

deepl = deepl.DeepL()

print(deepl.translate("Hello world!", dest="de"))
# ['Hallo Welt!', 'Hello world!', 'Guten Tag, Welt!']
```

### Documentation

There is only one function call in this library at the moment.

`translate(text, dest, src)`

The `dest` and `src` parameters are optional. The source language is detected by default and English is used as the default destination language.

Languages supported:

```
"en" - English
"de" - German
"fr" - French
"es" - Spanish
"pt" - Portuguese
"it" - Italian
"nl" - Dutch
"pl" - Polish
"ru" - Russian
```


### Troubleshooting

If you encounter a problem where you are getting empty results, you should consider increasing the delay of which the webpage is parsed.

`deepl.py`
```python
class Config:
    delay = 3 # increase this value
```

DISCLAIMER: This is an unofficial library and is not associated with DeepL.