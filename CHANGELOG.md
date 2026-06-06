# 更新日志

## 2026-06-06 - Gmail Android/Appium 本地注册包

**新增**
- 新增 `gmail_android/` 模块，包含 Gmail Android 注册流程、Appium helper API、`.env` 配置加载、SMS provider 骨架和 Windows 安装脚本。
- 新增 BlueStacks 直接安装/配置脚本：`gmail_android/scripts/install_bluestacks.ps1`，支持配置 ADB、`Pie64_12`、`127.0.0.1:5675`、`900x1600 @ 240dpi`。
- 新增一键安装入口：`gmail_android/scripts/install_all_windows.ps1`，用于 GitHub Release 安装包解压后的环境初始化。
- 新增 Release 构建脚本：`gmail_android/scripts/build_release.ps1`，支持可选附带固定版本 BlueStacks 安装器。
- 新增 `gmail_android/offline/bluestacks/.gitkeep`，预留固定版本 BlueStacks 安装器目录；安装器二进制不进 git，后续随 Release 附件打包。

**优化**
- 根 `.env.example` 增加 Gmail Android/Appium 相关环境变量：`APPIUM_SERVER`、`ANDROID_DEVICE`、`GMAIL_USERNAME_PREFIX`、`ACCEPT_TERMS`、`SMS_PROJECT_ID_GMAIL`、`HERO_SMS_SERVICE_GMAIL` 等。
- 根 `requirements.txt` 增加 `Appium-Python-Client` 和 `selenium`。
- 根 README 增加 Gmail Android 安装包的安装、配置、运行和 Release 打包说明。

**安全边界**
- Gmail 手机/SMS/CAPTCHA 和 Google 额外安全验证默认由人工完成；脚本支持 `--resume-after-phone` 续跑。
- `--accept-terms` 仅在操作者明确同意 Google Privacy and Terms 后使用。
- `sms_provider.py` 仅作为后续合规内部接码 provider 的环境变量接口骨架，当前不默认接入 Gmail 安全验证自动化。

## 2026-06-04 — Codex 订阅授权 + 上传 SUB2API / CPA

**新增**
- **`oauth_codex.py`**：账号走 Codex OAuth 换取**带 `refresh_token` 的正式凭据**，一步建到
  **SUB2API**（`type=oauth`）并推 **CPA**，解决网页 session 无 refresh_token、下游过期 401。
- **接码支持 WhatsApp**：遇 OpenAI add-phone 手机验证，用 `--manual-phone` 在浏览器手动填号 +
  输码，**推荐 WhatsApp 可接码号段**（普通虚拟号易被拒）。
- 配套：`activate_plus.py` 激活码开通 Plus / Codex 订阅；`upload_tokens.py` 一键上传到
  CPA / SUB2API / webchat2api。
- 订阅地址 / 激活码全部走环境变量（见 `.env.example`）。

**优化**
- README 补全「Codex 订阅授权 & token 上传」「项目结构 / 模块职责」「典型一条龙用法」，适配多人协作。
- 清理冗余代码，半成品路径标注 WIP。



