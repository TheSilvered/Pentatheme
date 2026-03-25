import json


class Theme:
    def __init__(self, name: str, colors: dict[str, str]):
        self.name = name

        self.background = colors["background"]
        self.row_background = colors["row_background"]
        self.border = colors["border"]
        self.input_border = colors["input_border"]

        self.workbench_fg = colors["workbench_fg"]
        self.editor_fg = colors["editor_fg"]
        self.muted_fg = colors["muted_fg"]
        self.light_fg = colors["light_fg"]

        self.accent = colors["accent"]
        self.accent_light = colors["accent_light"]

        self.yellow = colors["yellow"]
        self.orange = colors["orange"]
        self.light_red = colors["light_red"]
        self.dark_red = colors["dark_red"]
        self.light_green = colors["light_green"]
        self.dark_green = colors["dark_green"]
        self.light_blue = colors["light_blue"]
        self.dark_blue = colors["dark_blue"]
        self.light_cyan = colors["light_cyan"]
        self.dark_cyan = colors["dark_cyan"]
        self.purple = colors["purple"]
        self.violet = colors["violet"]
        self.black = colors["black"]
        self.dark_gray = colors["dark_gray"]
        self.light_gray = colors["light_gray"]
        self.white = colors["white"]

        self.keywords = colors[colors["keywords"]]
        self.constants = colors[colors["constants"]]
        self.strings = colors[colors["strings"]]

        self.hidden = "#0000"

        self.sel_alpha = colors["sel_alpha"]
        self.light_sel_alpha = colors["light_sel_alpha"]
        self.bg_sel_alpha = colors["bg_sel_alpha"]

    def dump(self, file):
        theme = {
            "$schema": "vscode://schemas/color-theme",
            "name": self.name,
            "colors": {
                # ==================
                # Text
                # ==================

                "textBlockQuote.background": self.border,
                "textBlockQuote.border": self.input_border,
                "textCodeBlock.background": self.border,
                "textLink.activeForeground": self.light_blue,
                "textLink.foreground": self.light_blue,
                "textPreformat.foreground": self.workbench_fg,
                "textPreformat.background": self.background,
                "textSeparator.foreground": self.border,

                # ==================
                # Input
                # ==================

                "button.border": self.hidden,
                "button.background": self.accent,
                "button.foreground": self.light_fg,
                "button.hoverBackground": self.accent_light,
                "button.secondaryBackground": self.border,
                "button.secondaryForeground": self.workbench_fg,
                "button.secondaryHoverBackground": self.input_border,

                "dropdown.background": self.border,
                "dropdown.border": self.hidden,
                "dropdown.foreground": self.workbench_fg,
                "dropdown.listBackground": self.border,

                "input.background": self.border,
                "input.border": self.input_border,
                "input.foreground": self.workbench_fg,
                "input.placeholderForeground": self.muted_fg,
                "inputOption.activeBackground": self.accent,
                "inputOption.activeBorder": self.accent,

                "checkbox.background": self.border,
                "checkbox.border": self.input_border,
                "checkbox.foreground": self.workbench_fg,
                "checkbox.disabled.background": self.background,
                "checkbox.disabled.foreground": self.muted_fg,

                # Maybe TODO: radio buttons

                # ==================
                # Settings
                # ==================

                "settings.rowHoverBackground": self.background,
                "settings.focusedRowBackground": self.background,
                "settings.focusedRowBorder": self.hidden,
                "settings.dropdownBackground": self.border,
                "settings.dropdownListBorder": self.input_border,
                "settings.dropdownBorder": self.input_border,
                "settings.headerForeground": self.workbench_fg,
                "settings.modifiedItemIndicator": self.orange,

                "keybindingLabel.foreground": self.workbench_fg,
                "keybindingLabel.background": self.border,
                "keybindingLabel.border": self.input_border,
                "keybindingLabel.bottomBorder": self.input_border,
                "keybindingTable.headerBackground": self.row_background,
                "keybindingTable.rowsBackground": self.row_background,

                # ==================
                # Workbench
                # ==================

                "actionBar.toggledBackground": self.input_border,
                "activityBar.activeBorder": self.hidden,
                "activityBar.background": self.background,
                "activityBar.border": self.border,
                "activityBar.foreground": self.workbench_fg,
                "activityBar.inactiveForeground": self.muted_fg,
                "activityBarBadge.background": self.accent,
                "activityBarBadge.foreground": self.light_fg,
                "badge.background": self.accent,
                "badge.foreground": self.light_fg,
                "profileBadge.background": self.accent,
                "profileBadge.foreground": self.light_fg,

                "debugToolBar.background": self.background,
                "toolbar.hoverBackground": self.input_border,
                "toolbar.activeBackground": self.input_border,

                "menu.background": self.background,
                "menu.border": self.border,
                "menu.foreground": self.workbench_fg,
                "menu.selectionBackground": self.accent,
                "menu.selectionForeground": self.light_fg,
                "menu.separatorBackground": self.border,

                "notificationCenterHeader.background": self.background,
                "notificationCenterHeader.foreground": self.workbench_fg,
                "notifications.background": self.background,
                "notifications.border": self.border,
                "notifications.foreground": self.workbench_fg,
                "notificationsInfoIcon.foreground": self.light_blue,
                "notificationsWarningIcon.foreground": self.orange,
                "notificationsErrorIcon.foreground": self.light_red,

                "pickerGroup.border": self.input_border,

                "quickInput.background": self.background,
                "quickInput.foreground": self.workbench_fg,

                "scrollbar.background": self.hidden,
                "scrollbar.shadow": self.black + "80",
                "scrollbarSlider.background": self.muted_fg + "40",
                "scrollbarSlider.hoverBackground": self.muted_fg + "60",
                "scrollbarSlider.activeBackground": self.muted_fg + "80",

                "sideBar.background": self.background,
                "sideBar.border": self.border,
                "sideBar.foreground": self.workbench_fg,
                "sideBarSectionHeader.background": self.background,
                "sideBarSectionHeader.border": self.border,
                "sideBarSectionHeader.foreground": self.workbench_fg,
                "sideBarTitle.foreground": self.workbench_fg,

                "statusBarItem.hoverBackground": self.input_border,
                "statusBarItem.hoverForeground": self.workbench_fg,
                "statusBar.debuggingBackground": self.accent,
                "statusBar.debuggingForeground": self.light_fg,
                "statusBar.focusBorder": self.accent,
                "statusBar.foreground": self.workbench_fg,
                "statusBar.noFolderBackground": self.background,
                "statusBarItem.focusBorder": self.accent,
                "statusBarItem.prominentBackground": self.hidden,
                "statusBarItem.remoteBackground": self.accent,
                "statusBarItem.remoteForeground": self.light_fg,
                "statusBar.background": self.background,
                "statusBar.border": self.border,

                "titleBar.activeBackground": self.background,
                "titleBar.activeForeground": self.workbench_fg,
                "titleBar.border": self.border,
                "titleBar.inactiveBackground": self.background,
                "titleBar.inactiveForeground": self.muted_fg,

                "welcomePage.tileBackground": self.border,
                "welcomePage.progress.foreground": self.accent,
                "welcomePage.progress.background": self.input_border,
                "welcomePage.tileBorder": self.hidden,
                "welcomePage.tileHoverBackground": self.input_border,

                # ==================
                # Lists
                # ==================

                "list.dropBackground": self.accent + self.sel_alpha,
                "list.activeSelectionBackground": self.accent + self.bg_sel_alpha,
                "list.hoverBackground": self.border,
                "list.activeSelectionForeground": self.workbench_fg,
                "list.inactiveFocusBackground": self.border,
                "list.inactiveSelectionBackground": self.border,
                "list.warningForeground": self.orange,
                "list.errorForeground": self.light_red,
                "list.deemphasizedForeground": self.muted_fg,
                "gitDecoration.modifiedResourceForeground": self.yellow,
                "gitDecoration.addedResourceForeground": self.light_green,
                "gitDecoration.deletedResourceForeground": self.light_red,
                "gitDecoration.conflictingResourceForeground": self.orange,
                "gitDecoration.renamedResourceForeground": self.light_green,
                "gitDecoration.ignoredResourceForeground": self.muted_fg,
                "gitDecoration.untrackedResourceForeground": self.light_green,
                "gitDecoration.submoduleResourceForeground": self.light_blue,
                "gitDecoration.stageDeletedResourceForeground": self.light_red,
                "gitDecoration.stageModifiedResourceForeground": self.yellow,

                "tree.tableOddRowsBackground": self.row_background,

                # ==================
                # Base colors
                # ==================

                "focusBorder": self.accent,
                "foreground": self.workbench_fg,
                "disabledForeground": self.muted_fg,
                "descriptionForeground": self.workbench_fg,
                "errorForeground": self.light_red,
                "selection.background": self.accent + self.sel_alpha,
                "widget.border": self.border,
                "widget.shadow": self.black + "30",
                "icon.foreground": self.workbench_fg,

                # ==================
                # Editor
                # ==================

                "editor.background": self.background,
                "editor.foreground": self.editor_fg,
                "editor.placeholder.foreground": self.muted_fg,
                "editor.foldPlaceholderForeground": self.muted_fg,
                "editor.foldBackground": self.muted_fg + "20",
                "editor.findMatchBackground": self.accent + self.light_sel_alpha, # selected match
                "editor.findMatchHighlightBackground": self.accent + self.light_sel_alpha, # other matches
                "editor.findMatchBorder": self.light_blue,
                "editor.rangeHighlightBackground": self.hidden,

                "editor.selectionBackground": self.accent + self.sel_alpha,
                "editor.inactiveSelectionBackground": self.accent + self.light_sel_alpha,
                "editor.selectionHighlightBackground": self.accent + self.light_sel_alpha,
                "editor.wordHighlightBackground": self.muted_fg + self.bg_sel_alpha,
                "editor.wordHighlightStrongBackground": self.accent + self.bg_sel_alpha,

                "editor.inlineValuesBackground": self.accent + self.light_sel_alpha,
                "editor.inlineValuesForeground": self.workbench_fg,
                "editor.stackFrameHighlightBackground": self.accent + self.light_sel_alpha,

                "editorGroup.border": self.border,
                "editorGroupHeader.tabsBackground": self.background,
                "editorGroupHeader.tabsBorder": self.background,
                "editorGroup.dropBackground": self.accent + self.sel_alpha,
                "editorGutter.addedBackground": self.light_green,
                "editorGutter.deletedBackground": self.light_red,
                "editorGutter.modifiedBackground": self.yellow,
                "editorIndentGuide.background1": self.border,
                "editorIndentGuide.activeBackground1": self.input_border,
                "editorRuler.foreground": self.input_border,
                "editorLineNumber.activeForeground": self.editor_fg,
                "editorLineNumber.foreground": self.muted_fg,
                "editorOverviewRuler.border": self.border,
                "editorWidget.background": self.background,

                "diffEditor.border": self.border,
                "diffEditor.diagonalFill": self.input_border,
                "diffEditor.insertedLineBackground": self.dark_green + self.bg_sel_alpha,
                "diffEditor.insertedTextBackground": self.dark_green + self.light_sel_alpha,
                "diffEditor.removedLineBackground": self.dark_red + self.bg_sel_alpha,
                "diffEditor.removedTextBackground": self.dark_red + self.light_sel_alpha,

                # ==================
                # Tabs
                # ==================

                "tab.activeBackground": self.background,
                "tab.activeBorder": self.accent,
                "tab.activeBorderTop": self.background,
                "tab.activeForeground": self.workbench_fg,
                "tab.selectedBackground": self.border,
                "tab.selectedBorderTop": self.background,
                "tab.selectedForeground": self.workbench_fg,
                "tab.border": self.background,
                "tab.hoverBackground": self.background,
                "tab.inactiveBackground": self.background,
                "tab.inactiveForeground": self.muted_fg,
                "tab.lastPinnedBorder": self.background,
                "tab.unfocusedActiveBorder": self.background,
                "tab.unfocusedActiveBorderTop": self.border,
                "tab.unfocusedHoverBackground": self.background,

                # ==================
                # Terminal
                # ==================

                "terminal.tab.activeBorder": self.accent,
                "terminal.foreground": self.editor_fg,
                "terminal.ansiBlack": self.black,
                "terminal.ansiBrightBlack": self.dark_gray,
                "terminal.ansiWhite": self.light_gray,
                "terminal.ansiBrightWhite": self.white,
                "terminal.ansiRed": self.dark_red,
                "terminal.ansiBrightRed": self.light_red,
                "terminal.ansiGreen": self.dark_green,
                "terminal.ansiBrightGreen": self.light_green,
                "terminal.ansiBlue": self.dark_blue,
                "terminal.ansiBrightBlue": self.light_blue,
                "terminal.ansiYellow": self.orange,
                "terminal.ansiBrightYellow": self.yellow,
                "terminal.ansiCyan": self.dark_cyan,
                "terminal.ansiBrightCyan": self.light_cyan,
                "terminal.ansiMagenta": self.purple,
                "terminal.ansiBrightMagenta": self.violet,

                # ==================
                # Panels
                # ==================

                "panel.background": self.background,
                "panel.border": self.border,
                "panelInput.border": self.input_border,
                "panelTitle.border": self.border,
                "panelTitle.activeBorder": self.accent,
                "panelTitle.activeForeground": self.workbench_fg,
                "panelTitle.inactiveForeground": self.muted_fg,

                "ports.iconRunningProcessForeground": self.dark_green,

                # ==================
                # Peek view
                # ==================

                "peekViewEditor.background": self.row_background,
                "peekViewEditor.matchHighlightBackground": self.accent + self.light_sel_alpha,
                "peekViewEditor.matchHighlightBorder": self.accent,
                "peekViewResult.background": self.background,
                "peekViewResult.matchHighlightBackground": self.accent + self.light_sel_alpha,
                "peekViewResult.fileForeground": self.workbench_fg,
                "peekViewResult.selectionBackground": self.accent + self.sel_alpha,
                "peekViewResult.lineForeground": self.workbench_fg,
                "peekViewResult.selectionForeground": self.light_fg,
                "peekView.border": self.border,

                # ==================
                # Chat
                # ==================

                "chat.slashCommandForeground": self.light_blue,
                "chat.slashCommandBackground": self.accent + self.light_sel_alpha,
                "chat.editedFileForeground": self.yellow,
            },
            "tokenColors": [
                {
                    "scope": [
                        "emphasis",
                        "markup.italic"
                    ],
                    "settings": {
                        "fontStyle": "italic"
                    }
                },
                {
                    "scope": [
                        "strong",
                        "markup.bold"
                    ],
                    "settings": {
                        "fontStyle": "bold"
                    }
                },
                {
                    "scope": "comment",
                    "settings": {
                        "foreground": self.muted_fg
                    }
                },
                {
                    "scope": "string",
                    "settings": {
                        "foreground": self.strings
                    }
                },
                {
                    "scope": "constant",
                    "settings": {
                        "foreground": self.constants
                    }
                },
                {
                    "scope": [
                        "keyword",
                        "storage"
                    ],
                    "settings": {
                        "foreground": self.keywords
                    }
                }
            ]
        }
        json.dump(theme, file, indent=4)


dark_colors = {
    "background": "#151515",
    "row_background": "#1c1c1c",
    "border": "#212121",
    "input_border": "#303030",
    "workbench_fg": "#d0d0d0",
    "editor_fg": "#cbcbcb",
    "muted_fg": "#747474",
    "light_fg": "#f0f0f0",
    "yellow": "#f1d77f",
    "orange": "#e6a328",
    "light_red": "#f36e67",
    "dark_red": "#cf251c",
    "light_green": "#7bb361",
    "dark_green": "#57943b",
    "light_blue": "#4ba8f0",
    "dark_blue": "#0164af",
    "light_cyan": "#4edace",
    "dark_cyan": "#16a99d",
    "purple": "#a01ee1",
    "violet": "#c070e8",
    "black": "#000000",
    "dark_gray": "#747474",
    "light_gray": "#d0d0d0",
    "white": "#f0f0f0",
    "accent": "#0164af",
    "accent_light": "#0e7bce",

    "keywords": "light_blue",
    "constants": "orange",
    "strings": "light_green",

    "sel_alpha": "b0",
    "light_sel_alpha": "50",
    "bg_sel_alpha": "40"
}

light_colors = {
    "background": "#f6f6f6",
    "row_background": "#efefef",
    "border": "#ececec",
    "input_border": "#d0d0d0",
    "workbench_fg": "#151515",
    "editor_fg": "#353535",
    "muted_fg": "#999999",
    "light_fg": "#fff",
    "yellow": "#d1a000",
    "orange": "#a86d00",
    "light_red": "#ee5a52",
    "dark_red": "#cf251c",
    "light_green": "#66ac46",
    "dark_green": "#448525",
    "light_blue": "#1b98f7",
    "dark_blue": "#0164af",
    "light_cyan": "#2dc9bc",
    "dark_cyan": "#0a8b81",
    "purple": "#a01ee1",
    "violet": "#c070e8",
    "black": "#000000",
    "dark_gray": "#999999",
    "light_gray": "#d0d0d0",
    "white": "#ffffff",
    "accent": "#1b98f7",
    "accent_light": "#1f7cc4",

    "keywords": "light_blue",
    "constants": "yellow",
    "strings": "light_green",

    "sel_alpha": "50",
    "light_sel_alpha": "30",
    "bg_sel_alpha": "28"
}

theme_dark = Theme("Pentatheme Dark", dark_colors)
theme_light = Theme("Pentatheme Light", light_colors)

with open("themes/theme-dark.json", "w") as f:
    theme_dark.dump(f)
with open("themes/theme-light.json", "w") as f:
    theme_light.dump(f)
