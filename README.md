<p align="center">
  <img src="https://raw.githubusercontent.com/vaxicy/wheat-clay-theme/main/assets/icon.png" alt="Wheat Clay Theme logo" width="128">
</p>

<h1 align="center">Wheat Clay Theme</h1>

<p align="center">
  <a href="https://marketplace.visualstudio.com/items?itemName=lilinhuang.wheat-clay-theme"><img src="https://img.shields.io/badge/VS%20Code-Theme-8A7F6A?logo=visual-studio-code" alt="VS Code Theme"></a>
  <img src="https://img.shields.io/badge/version-1.0.0-B7B09E?logo=visual-studio-code" alt="version 1.0.0">
  <img src="https://img.shields.io/badge/Variants-Light%20%26%20Dark-CFC6B1?logo=visual-studio-code" alt="Light and Dark variants">
  <a href="https://github.com/vaxicy/wheat-clay-theme/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-Non--Commercial-lightgrey" alt="License: Non-Commercial"></a>
</p>

Warm neutral paper: **oat and khaki** tones in the light variant, and a **stone-brown night** in the dark one. One palette of four earth shades, so switching changes the hour rather than the material.

暖中性纸感主题：浅色版是**燕麦与卡其**色阶，深色版是**石褐色夜晚**。一套四个大地色贯穿明暗两版，切换的是时辰，不是材质。

## Preview / 预览

| Light 浅色 | Dark 深色 |
| --- | --- |
| ![Wheat Clay Theme Light](https://raw.githubusercontent.com/vaxicy/wheat-clay-theme/main/store-assets/screenshots/en/screenshot-light.png) | ![Wheat Clay Theme Dark](https://raw.githubusercontent.com/vaxicy/wheat-clay-theme/main/store-assets/screenshots/en/screenshot-dark.png) |

> Both previews are captured from a real VS Code window running the theme — no mockups.
>
> 上方预览图取自真实运行该主题的 VS Code 窗口截图，非模拟图。

## Palette / 色板

| Role | Light | Dark |
| --- | --- | --- |
| Editor background | `#FCF7EA` oat paper | `#3C3830` stone night |
| Foreground | `#3B3327` clay ink | `#EFE7D6` warm cream |
| Muted text / placeholders | `#9A907E` | `#A89D8A` |
| Side bar | `#FAF5EA` | `#37332B` |
| Panel / terminal | `#FBF7EC` | `#39352C` |
| Title bar | `#EBE2CC` paper with `#3B3327` text | `#302D26` with `#DCD3C0` text |
| Tab bar / inactive tab | `#F2ECDD` | `#39352C` |
| Active tab / indicator | `#332C21` text, `#8A7F6A` top border | `#F2EBDC` text, `#CFC6B1` top border |
| Activity bar | `#F3EDE0` with `#6B6250` icons | `#35312A` with `#C4B89E` icons |
| Status bar | `#6B6250` with `#F5EFE2` text | `#5A5245` with `#F2EBDC` text |
| Selection | `#DED6C1` oat | `#524B3F` |
| Current line | `#FAF4E6` | `#464136` |
| Borders | `#E6DECC` | `#5A5347` |
| Indent guides | `#EAE3D2` | `#4A4438` |
| Button | `#6B6250` with white text (hover `#5A5243`) | `#CFC6B1` with `#302D26` text (hover `#DED6C1`) |
| Badge | `#6B6250` with white text | `#CFC6B1` with `#302D26` text |
| Cursor | `#6B6250` | `#CFC6B1` |
| Links | `#6B6250` | `#CFC6B1` |
| Errors / warnings | `#A0554A` / `#8A6B3A` | `#EBA8A0` / `#E8C88A` |
| Git added / modified / deleted | `#5E7A52` / `#8A6B3A` / `#A0554A` | `#B8D8A8` / `#E8C88A` / `#EBA8A0` |

Paper `#EBE2CC`, oat `#DED6C1`, khaki `#CFC6B1` and stone `#B7B09E` carry both variants, so a file still reads as "wheat clay" after switching.

纸米 `#EBE2CC`、燕麦 `#DED6C1`、卡其 `#CFC6B1` 与石色 `#B7B09E` 贯穿明暗两版，切换后整个文件还是同一种土色。

## Syntax mapping / 语法映射

| Syntax | Light | Dark |
| --- | --- | --- |
| Comments | `#9A907E` | `#9C9280` |
| Keywords / storage | `#6B5F4A` | `#D8C9A8` |
| Strings | `#8A6B3A` | `#E8CE96` |
| Functions / methods | `#5E6E5A` | `#B8CCB0` |
| Types / classes | `#7A6350` | `#D8BFA8` |
| Numbers / constants | `#A0793F` | `#E8C88A` |
| Variables | `#3B3327` | `#EFE7D6` |
| Parameters | `#5E5344` | `#C9BFA8` |
| Properties | `#5E6E5A` | `#B8CCB0` |
| Operators | `#7E7361` | `#C4BAA8` |
| Punctuation | `#9A907E` | `#9C9280` |
| HTML tags | `#6B5F4A` | `#D8C9A8` |
| Attribute names | `#A0793F` | `#E8C88A` |
| Regex | `#8A6B3A` | `#DCC48A` |
| Escape characters | `#A0793F` | `#EFD9AE` |

Semantic highlighting is enabled, so variables, parameters, properties, functions and types follow the same mapping in TypeScript, JavaScript, Go, Rust and Python.

已开启语义高亮，TypeScript、JavaScript、Go、Rust 与 Python 里的变量、参数、属性、函数与类型都会落到同一套配色。

## Install / 安装

1. 打开扩展面板 `Ctrl+Shift+X`。
2. 搜索 **Wheat Clay Theme** 并安装。
3. 按 `Ctrl+K Ctrl+T`，选择 `Wheat Clay Theme Light` 或 `Wheat Clay Theme Dark`。

也可以用命令行安装：

```bash
code --install-extension lilinhuang.wheat-clay-theme
```

## Build from source / 本地构建

```bash
py -3 scripts/build-theme.py       # regenerate both theme JSON files
py -3 scripts/generate-icon.py     # export assets/icon.png from the selected logo
py -3 scripts/capture-real-screenshots.py   # real VS Code screenshots
```

## License / 许可证

Non-Commercial License — free for personal, educational and non-commercial use. See [LICENSE](https://github.com/vaxicy/wheat-clay-theme/blob/main/LICENSE).

非商业许可证：个人、教育与非商业用途免费使用，详见 LICENSE。
