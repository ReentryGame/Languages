# Languages
This repo contains the current language support of the game UI/mechanics of Reentry.

## Status
The following section will contain the status of the translation of the UI.

MainMenuUI
- [X] English/US
- [X] Spanish
- [X] Russian
- [X] French
- [X] German
- [X] Chinese (Simplified)
- [X] Portuguese of Brazil
- [ ] Japanese

CommonUI
- [X] English/US
- [X] Spanish
- [X] Russian
- [X] French
- [X] German
- [X] Chinese (Simplified)
- [X] Portuguese of Brazil
- [ ] Japanese

MercuryGame
- [X] English/US
- [X] Spanish
- [X] Russian
- [X] French
- [X] German
- [X] Chinese (Simplified)
- [X] Portuguese of Brazil
- [ ] Japanese

GeminiGame
- [X] English/US
- [X] Spanish
- [X] Russian
- [X] French
- [X] German
- [X] Chinese (Simplified)
- [X] Portuguese of Brazil
- [ ] Japanese

ApolloGame
- [X] English/US
- [X] Spanish
- [X] Russian
- [X] French
- [X] German
- [X] Chinese (Simplified)
- [X] Portuguese of Brazil
- [ ] Japanese

The following list shows the languages we currently want to support. More will be added as the core of the game gets translated. If you have suggestions please reach out.
|        Language        | code  |
|------------------------|-------|
| Spanish                | es-es |
| Russian                | ru-ru |
| French                 | fr-fr |
| German                 | de-de |
| Chinese (Simplified)   | zh-cn |
| Portuguese of Brazil   | pt-br |
| Japanese               | ja-ja |

## How to contribute
To contribute, you will need to get the language files stored on your harddrive, pick a language to translate to for a given file that is missing in the status above, use the in-game tool to translate (or a text editor), then commit and push the change as a pull request. We will then test and verify, and potentially merge the change into the game.

### 1. Setup
The first step you need to do is to clone or download this repo to your local environment.
Do this by using the clone/download zip button on this repo (Code->Clone/Download Zip)

When you have the repo cloned, all of the language UI files can be found in various directories. These files are used by the game to look up what a text element on the UI will contain.
These files can be opened by the Reentry Language UI tool  (Main Menu->Contribute->Translate UI).

### 2. Structure
The data is stored in different language files. The Main Menu has one file, and each of the supported modules have their own language file(s), and a common that is shared between all of them.
The default language is en-us. This can be seen in the file name:
MainMenuUI.**en-us**.json

For the game to would support another language such as de-de (German (Germany)), the english file would need to be translated to German, and saved as:
MainMenuUI.**de-de**.json

### 3. Translate
Copy the absolute path and the file name of the file you want to translate (english base file). For example:
C:\repos\Reentry\languages\MainMenuUI.en-us.json

Start Reentry, and press CONTRIBUTE on the Main Menu, then launch the TRANSLATE GAME UI tool.
Paste the absolute path to the file you wish to translate and press LOAD.

When loaded, you can either start a new translation by inserting the language code (see table above) that you wish to translate to, or load an existing translation by pressing Continue and pasting in the absolute path to the target language file such as:
C:\repos\Reentry\languages\MainMenuUI.de-de.json

When done, press SAVE.

### 4. Contributing your changes
The last step is to submit your changes to us. This is done through a pull request.

Forking a repo
https://docs.github.com/en/get-started/quickstart/fork-a-repo

Submitting your fork as a pull request to the language repo
https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork

For language-codes, see [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) and [ISO 3166-1](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) alpha-2. For example, for English as written in the United States, first lookup the ISO 3166-1 alpha 2 code for the United States (**us**), then the ISO 639-1 language-code for English (**en**). For constructed languages, see [ISO-639-2](https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes). For languages that do not belong to a specific country (ex latin), use the language-code as previously specified without a country-code.
