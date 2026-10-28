# -*- coding: utf-8 -*-
"""Build the Wheat Clay Light / Dark color themes from one palette table.

    py -3 scripts/build-theme.py
"""

import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
THEMES = BASE / "themes"
NAME = "wheat-clay-theme"
SLUG = "wheat-clay"
DISPLAY = "Wheat Clay Theme"
VERSION = "1.0.0"
REPO = "https://github.com/vaxicy/wheat-clay-theme"

UI = {
    "foreground": ("#3B3327", "#EFE7D6"),
    "editor.foreground": ("#3B3327", "#EFE7D6"),
    "terminal.foreground": ("#3B3327", "#EFE7D6"),
    "input.foreground": ("#332C21", "#F7F0E0"),
    "dropdown.foreground": ("#332C21", "#F7F0E0"),
    "quickInput.foreground": ("#332C21", "#F7F0E0"),
    "editorWidget.foreground": ("#332C21", "#F7F0E0"),
    "editorHoverWidget.foreground": ("#332C21", "#F7F0E0"),
    "editorSuggestWidget.foreground": ("#332C21", "#F7F0E0"),
    "notifications.foreground": ("#332C21", "#F7F0E0"),
    "descriptionForeground": ("#9A907E", "#A89D8A"),
    "input.placeholderForeground": ("#9A907E", "#A89D8A"),
    "focusBorder": ("#6B6250", "#CFC6B1"),
    "inputOption.activeBorder": ("#5A5243", "#DED6C1"),
    "input.border": ("#E6DECC", "#5A5347"),
    "dropdown.border": ("#E6DECC", "#5A5347"),
    "editor.background": ("#FCF7EA", "#3C3830"),
    "tab.activeBackground": ("#FCF7EA", "#3C3830"),
    "titleBar.activeBackground": ("#EBE2CC", "#302D26"),
    "titleBar.activeForeground": ("#3B3327", "#DCD3C0"),
    "titleBar.inactiveBackground": ("#F2ECDB", "#35312A"),
    "titleBar.inactiveForeground": ("#877C69", "#A29785"),
    "activityBar.background": ("#F3EDE0", "#35312A"),
    "activityBar.foreground": ("#6B6250", "#C4B89E"),
    "activityBar.activeBorder": ("#6B6250", "#CFC6B1"),
    "activityBar.inactiveForeground": ("#A89D8A", "#857A67"),
    "sideBar.background": ("#FAF5EA", "#37332B"),
    "sideBar.foreground": ("#4A4133", "#DED6C3"),
    "sideBarSectionHeader.background": ("#F2ECDD", "#403B32"),
    "sideBarSectionHeader.foreground": ("#544A3B", "#E7DFCE"),
    "panel.background": ("#FBF7EC", "#39352C"),
    "terminal.background": ("#FBF7EC", "#39352C"),
    "panel.border": ("#E6DECC", "#5A5347"),
    "editorGroup.border": ("#E6DECC", "#5A5347"),
    "tab.border": ("#E6DECC", "#5A5347"),
    "sideBar.border": ("#E6DECC", "#5A5347"),
    "titleBar.border": ("#E6DECC", "#5A5347"),
    "statusBar.background": ("#6B6250", "#5A5245"),
    "statusBar.noFolderBackground": ("#6B6250", "#5A5245"),
    "statusBar.foreground": ("#F5EFE2", "#F2EBDC"),
    "statusBar.noFolderForeground": ("#F5EFE2", "#F2EBDC"),
    "statusBarItem.hoverBackground": ("#7A7060", "#68604F"),
    "statusBar.debuggingBackground": ("#8A5A3A", "#8A6448"),
    "statusBar.debuggingForeground": ("#FBF4EA", "#F7EDE0"),
    "editorGroupHeader.tabsBackground": ("#F2ECDD", "#39352C"),
    "tab.inactiveBackground": ("#F2ECDD", "#39352C"),
    "tab.activeForeground": ("#332C21", "#F2EBDC"),
    "tab.activeBorderTop": ("#8A7F6A", "#CFC6B1"),
    "tab.inactiveForeground": ("#9A907E", "#A29785"),
    "tab.hoverBackground": ("#F6F0E2", "#403B32"),
    "tab.activeModifiedBorder": ("#8A6B3A", "#E8C88A"),
    "tab.inactiveModifiedBorder": ("#8A6B3A", "#E8C88A"),
    "list.hoverBackground": ("#F8F2E4", "#403B32"),
    "list.activeSelectionBackground": ("#DED6C1", "#524B3F"),
    "editorSuggestWidget.selectedBackground": ("#DED6C1", "#524B3F"),
    "list.activeSelectionForeground": ("#332C21", "#F2EBDC"),
    "list.inactiveSelectionForeground": ("#332C21", "#F2EBDC"),
    "editorSuggestWidget.selectedForeground": ("#332C21", "#F2EBDC"),
    "list.inactiveSelectionBackground": ("#E9E2D0", "#4A4438"),
    "list.highlightForeground": ("#6B6250", "#CFC6B1"),
    "list.focusHighlightForeground": ("#6B6250", "#CFC6B1"),
    "tree.indentGuidesStroke": ("#E9E1D0", "#524B3F"),
    "editorLineNumber.foreground": ("#B5A996", "#857A67"),
    "editorLineNumber.activeForeground": ("#6B6250", "#CFC6B1"),
    "editor.lineHighlightBackground": ("#FAF4E6", "#464136"),
    "editor.lineHighlightBorder": ("#F0E9D7", "#4F493D"),
    "editorCursor.foreground": ("#6B6250", "#CFC6B1"),
    "selection.background": ("#DED6C1", "#524B3F"),
    "editor.selectionBackground": ("#DED6C1", "#524B3F"),
    "terminal.selectionBackground": ("#DED6C1", "#524B3F"),
    "editor.inactiveSelectionBackground": ("#E9E2D0", "#4A4438"),
    "editor.wordHighlightBackground": ("#DED6C180", "#6E655580"),
    "editor.wordHighlightStrongBackground": ("#DED6C180", "#6E655580"),
    "editor.selectionHighlightBackground": ("#DED6C166", "#6E655566"),
    "editor.findMatchHighlightBackground": ("#EFE3C2", "#5E5748"),
    "editor.findMatchBackground": ("#E2D2A8", "#6E6555"),
    "editor.findMatchBorder": ("#6B6250", "#DED6C1"),
    "editorBracketMatch.background": ("#F0E9D7", "#4A4438"),
    "editorBracketMatch.border": ("#8A7F6A", "#B7B09E"),
    "editorIndentGuide.background1": ("#EAE3D2", "#4A4438"),
    "editorIndentGuide.activeBackground1": ("#B7B09E", "#8A7F6A"),
    "editorWhitespace.foreground": ("#E9E1D0", "#524B3F"),
    "editorRuler.foreground": ("#F4EDDD", "#464136"),
    "textLink.foreground": ("#6B6250", "#CFC6B1"),
    "textLink.activeForeground": ("#5A5243", "#DED6C1"),
    "editorLink.activeForeground": ("#5A5243", "#DED6C1"),
    "quickInput.background": ("#FEFAF0", "#403B32"),
    "editorHoverWidget.background": ("#FEFAF0", "#403B32"),
    "notifications.background": ("#FEFAF0", "#403B32"),
    "input.background": ("#FFFCF4", "#37332B"),
    "dropdown.background": ("#FFFCF4", "#37332B"),
    "editorWidget.background": ("#FEFAF0", "#403B32"),
    "editorSuggestWidget.background": ("#FEFAF0", "#403B32"),
    "editorWidget.border": ("#E6DECC", "#60594B"),
    "editorHoverWidget.border": ("#E6DECC", "#60594B"),
    "editorSuggestWidget.border": ("#E6DECC", "#60594B"),
    "notifications.border": ("#E6DECC", "#60594B"),
    "button.background": ("#6B6250", "#CFC6B1"),
    "button.foreground": ("#FFFFFF", "#302D26"),
    "button.hoverBackground": ("#5A5243", "#DED6C1"),
    "button.secondaryBackground": ("#F2ECDD", "#4A4438"),
    "button.secondaryForeground": ("#4A4133", "#E7DFCE"),
    "button.secondaryHoverBackground": ("#EAE2D1", "#524B3F"),
    "badge.background": ("#6B6250", "#CFC6B1"),
    "activityBarBadge.background": ("#6B6250", "#CFC6B1"),
    "badge.foreground": ("#FFFFFF", "#302D26"),
    "activityBarBadge.foreground": ("#FFFFFF", "#302D26"),
    "scrollbarSlider.background": ("#B5A99666", "#A89D8A88"),
    "scrollbarSlider.hoverBackground": ("#A0938099", "#B8AD9A99"),
    "scrollbarSlider.activeBackground": ("#8A7D6A99", "#CFC6B199"),
    "errorForeground": ("#A0554A", "#EBA8A0"),
    "editorError.foreground": ("#A0554A", "#EBA8A0"),
    "problemsErrorIcon.foreground": ("#A0554A", "#EBA8A0"),
    "gitDecoration.deletedResourceForeground": ("#A0554A", "#EBA8A0"),
    "editorGutter.deletedBackground": ("#A0554A", "#EBA8A0"),
    "editorWarning.foreground": ("#8A6B3A", "#E8C88A"),
    "problemsWarningIcon.foreground": ("#8A6B3A", "#E8C88A"),
    "editorInfo.foreground": ("#5E6E5A", "#B8CCB0"),
    "problemsInfoIcon.foreground": ("#5E6E5A", "#B8CCB0"),
    "gitDecoration.addedResourceForeground": ("#5E7A52", "#B8D8A8"),
    "gitDecoration.untrackedResourceForeground": ("#5E7A52", "#B8D8A8"),
    "editorGutter.addedBackground": ("#5E7A52", "#B8D8A8"),
    "gitDecoration.modifiedResourceForeground": ("#8A6B3A", "#E8C88A"),
    "editorGutter.modifiedBackground": ("#8A6B3A", "#E8C88A"),
    "diffEditor.insertedTextBackground": ("#E2EAD6AA", "#4A443866"),
    "diffEditor.removedTextBackground": ("#EFDCD4AA", "#5E463E66"),
    "diffEditor.insertedLineBackground": ("#E2EAD666", "#4A443844"),
    "diffEditor.removedLineBackground": ("#EFDCD466", "#5E463E44"),
    "terminal.ansiBlack": ("#3B3327", "#403B32"),
    "terminal.ansiRed": ("#A0554A", "#EBA8A0"),
    "terminal.ansiGreen": ("#5E7A52", "#B8D8A8"),
    "terminal.ansiYellow": ("#8A6B3A", "#E8C88A"),
    "terminal.ansiBlue": ("#5E6E7A", "#B8C8D4"),
    "terminal.ansiMagenta": ("#7A5F6E", "#D8BCCB"),
    "terminal.ansiCyan": ("#5E7A72", "#B8D4CC"),
    "terminal.ansiWhite": ("#9A907E", "#DED6C3"),
    "terminal.ansiBrightBlack": ("#7A7060", "#857A67"),
    "terminal.ansiBrightRed": ("#BC6A5C", "#F7C0B4"),
    "terminal.ansiBrightGreen": ("#728E64", "#CBE4BC"),
    "terminal.ansiBrightYellow": ("#A08048", "#F0DCB0"),
    "terminal.ansiBrightBlue": ("#72828E", "#CCDCE8"),
    "terminal.ansiBrightMagenta": ("#8E7282", "#E8CEDC"),
    "terminal.ansiBrightCyan": ("#728E86", "#CCE4DC"),
    "terminal.ansiBrightWhite": ("#332C21", "#F7F0E0"),
}

TOKENS = [
    ("comment", ("#9A907E", "#9C9280"), "italic"),
    (("keyword", "storage"), ("#6B5F4A", "#D8C9A8"), None),
    ("string", ("#8A6B3A", "#E8CE96"), None),
    (("entity.name.function", "support.function"), ("#5E6E5A", "#B8CCB0"), None),
    (("entity.name.type", "support.type", "support.class"), ("#7A6350", "#D8BFA8"), None),
    (("constant.numeric", "constant.language", "variable.other.constant"), ("#A0793F", "#E8C88A"), None),
    ("variable", ("#3B3327", "#EFE7D6"), None),
    ("variable.parameter", ("#5E5344", "#C9BFA8"), None),
    (("variable.other.property", "support.variable.property"), ("#5E6E5A", "#B8CCB0"), None),
    ("keyword.operator", ("#7E7361", "#C4BAA8"), None),
    ("punctuation", ("#9A907E", "#9C9280"), None),
    ("entity.name.tag", ("#6B5F4A", "#D8C9A8"), None),
    ("entity.other.attribute-name", ("#A0793F", "#E8C88A"), None),
    ("string.regexp", ("#8A6B3A", "#DCC48A"), None),
    ("constant.character.escape", ("#A0793F", "#EFD9AE"), None),
    ("markup.heading", ("#332C21", "#F7F0E0"), "bold"),
    ("markup.bold", ("#332C21", "#F7F0E0"), "bold"),
    ("markup.italic", ("#332C21", "#F7F0E0"), "italic"),
    ("invalid", ("#A0554A", "#EBA8A0"), None),
]

SEMANTIC = {
    "variable": "#3B3327|#EFE7D6",
    "parameter": "#5E5344|#C9BFA8",
    "property": "#5E6E5A|#B8CCB0",
    "function": "#5E6E5A|#B8CCB0",
    "method": "#5E6E5A|#B8CCB0",
    "type": "#7A6350|#D8BFA8",
    "class": "#7A6350|#D8BFA8",
    "interface": "#7A6350|#D8BFA8",
    "variable.readonly": "#A0793F|#E8C88A",
}

PACKAGE = {
    "name": NAME,
    "displayName": DISPLAY,
    "description": "Warm neutral paper: oat and khaki tones in the light variant, a stone-brown night in the dark one.",
    "version": VERSION,
    "publisher": "lilinhuang",
    "engines": {"vscode": "^1.80.0"},
    "categories": ["Themes"],
    "keywords": ["theme", "light", "dark", "wheat", "clay"],
    "icon": "assets/icon.png",
    "license": "SEE LICENSE IN LICENSE",
    "galleryBanner": {"color": "#3C3830", "theme": "dark"},
    "repository": {"type": "git", "url": REPO},
    "contributes": {
        "themes": [
            {"label": f"{DISPLAY} Light", "uiTheme": "vs",
             "path": f"./themes/{SLUG}-light-color-theme.json"},
            {"label": f"{DISPLAY} Dark", "uiTheme": "vs-dark",
             "path": f"./themes/{SLUG}-dark-color-theme.json"},
        ]
    },
}


def build(variant, index):
    colors = {key: pair[index] for key, pair in UI.items()}
    tokens = []
    for scope, pair, style in TOKENS:
        settings = {"foreground": pair[index]}
        if style:
            settings["fontStyle"] = style
        tokens.append({"scope": [scope] if isinstance(scope, str) else list(scope),
                       "settings": settings})
    theme = {
        "name": f"{DISPLAY} {variant.title()}",
        "type": variant,
        "colors": colors,
        "semanticHighlighting": True,
        "semanticTokenColors": {k: v.split("|")[index] for k, v in SEMANTIC.items()},
        "tokenColors": tokens,
    }
    out = THEMES / f"{SLUG}-{variant}-color-theme.json"
    out.write_text(json.dumps(theme, indent=2) + "\n", encoding="utf-8")
    print("wrote", out.relative_to(BASE), len(colors), "UI colors")


def main():
    THEMES.mkdir(exist_ok=True)
    for index, variant in enumerate(("light", "dark")):
        build(variant, index)
    (BASE / "package.json").write_text(json.dumps(PACKAGE, indent=2) + "\n", encoding="utf-8")
    print("wrote package.json")


if __name__ == "__main__":
    main()
