# facebook_birthday_to_ics

Create an ICS file from Facebook birthdays

I couldn't get other solutions to work because of two-factor-authentication and trust issues. So I wrote this script to remember my friends' birthdays. The ICS file can be imported in common calendar applications.
It is written in simplest Python and does not perform any network communication, perfect for people with trust issues.

I tried it with English (US) and German locale setting on Facebook, may work for others as well.

## Instructions
1. Clone repo or just download Python script
2. Visit https://www.facebook.com/events/birthdays/
3. Scroll to bottom of page (so that all Facebook birthdays have been loaded)
4. Export HTML of page (see next chapter)
5. Run `python3 facebook_birthday_parser.py <PATH TO YOUR HTML EXPORT>`
6. Import `birthdays.ics` in your favorite calendar application

## Export HTML
Kinda tricky, because a simple Ctrl+S usually does not help. We need the dynamically loaded content as well, and Ctrl+S does not save the Javascript generated content.

### Option 1: Use a small Javascript
Full javascript:
```javascript
function download() {
    var f = new Blob([document.documentElement.innerHTML], {type: "text/html"});
    if (window.navigator.msSaveOrOpenBlob) {
        window.navigator.msSaveOrOpenBlob(f, "birthdays.html");
    } else {
        var a = document.createElement("a"), u = URL.createObjectURL(f);
        a.href = u;
        a.download = "birthdays.html";
        a.click();
    }
}
```

Ready to copy:
`javascript: var f = new Blob([document.documentElement.innerHTML], {type: "text/html"}); if (window.navigator.msSaveOrOpenBlob) { window.navigator.msSaveOrOpenBlob(f, "birthdays.html"); } else { var a = document.createElement("a"), u = URL.createObjectURL(f); a.href = u; a.download = "birthdays.html"; a.click();`

Paste it in your browser's URL line. Works at least for me in Chrome, but not in newer Firefoxes.

### Option 2: Use the developer console
Chrome: Ctrl + Shift + J
Firefox: Ctrl + Shift + I

1. Right click on `<html ...`
2. Copy
3. Outer HTML
4. Paste it into a file

or use the above Javascript code in the console tab:
`var f = new Blob([document.documentElement.innerHTML], {type: "text/html"}); if (window.navigator.msSaveOrOpenBlob) { window.navigator.msSaveOrOpenBlob(f, "birthdays.html"); } else { var a = document.createElement("a"), url = URL.createObjectURL(f); a.href = url; a.download = "birthdays.html"; a.click();`

## Disclaimer
It may work, it may not. Do not trust this tool and better check Facebook before congratulating your friends. ;)
