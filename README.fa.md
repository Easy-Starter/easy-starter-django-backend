<div dir="rtl" align="right">

<div align="center">

# استارتر بک‌اند Django

**بک‌اند Production-capable با Django شامل ادمین، پایه‌ی API، PostgreSQL، Docker، تست و تنظیمات امن محیط.**

[![Use this template](https://img.shields.io/badge/Use%20this%20template-2ea44f?logo=github&logoColor=white)](https://github.com/easy-starter/easy-starter-django-backend/generate) [![CI](https://github.com/easy-starter/easy-starter-django-backend/actions/workflows/ci.yml/badge.svg)](https://github.com/easy-starter/easy-starter-django-backend/actions/workflows/ci.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) ![Status: foundation](https://img.shields.io/badge/status-foundation-orange) ![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white) ![uv](https://img.shields.io/badge/uv-DE5FE9?logo=uv&logoColor=black)

[English](README.md) · [مستندات](https://github.com/easy-starter/easy-starter-docs) · [گزارش مشکل](https://github.com/easy-starter/easy-starter-django-backend/issues/new/choose)

</div>

> [!IMPORTANT]
> این ریپوزیتوری در مرحله‌ی **Foundation** است. تا انتشار اولین نسخه‌ی پایدار، آن را Production-ready در نظر نگیرید.

## چه مشکلی را حل می‌کند؟

پایه‌ای یکپارچه برای بک‌اند فراهم می‌کند تا پروژه با تنظیمات امن، مرزهای مشخص اپ‌ها، توسعه‌ی محلی تکرارپذیر و کنترل‌های پروداکشن شروع شود.

## این تمپلیت برای چه پروژه‌هایی مناسب است؟

- REST API و بک‌اند کسب‌وکار
- عملیات مبتنی بر Django Admin
- بک‌اند Next.js، اپ موبایل، بات و افزونه
- محصولات داده‌محور و Workflow-driven

**مناسب این موارد نیست:** برای ساخت ناوگان Microservice یا تحمیل مدل دامنه‌ی آماده به همه‌ی کسب‌وکارها نیست.

## امکانات پایه

- Settings و اعتبارسنجی جدا برای محیط‌ها
- Custom User Model و پایه‌ی پنل ادمین
- PostgreSQL، Migration، Health Check و Structured Logging
- ورک‌فلوی Docker برای لوکال و پروداکشن
- تست، Lint، Type Check، CI و چک‌لیست استقرار

توضیحات جزئی معماری، قراردادها، پروفایل‌های استقرار و روش توسعه در [`docs/`](docs/) قرار می‌گیرند. توسعه‌ی فیچر از [`specs/`](specs/) شروع می‌شود و قوانین ایجنت‌ها در [`AGENTS.md`](AGENTS.md) نگهداری می‌شوند.

## شروع سریع

۱. روی **Use this template** بزنید یا فرمان زیر را اجرا کنید:

```bash
gh repo create my-project --template easy-starter/easy-starter-django-backend --private --clone
cd my-project
```

۲. نام پروژه، متادیتای پکیج و متغیرهای محیطی را تنظیم کنید.
۳. پروژه را اجرا کنید:

```bash
cp .env.example .env
make setup
make dev
make check
```

۴. اولین مشخصات فیچر را در `specs/` بنویسید.
۵. فیچر را پیاده‌سازی کنید و `make check` را سبز نگه دارید.

## قرارداد همکاری

- قبل از تغییر کد، `AGENTS.md` و Spec مرتبط را بخوانید.
- پیش از افزودن Abstraction یا Dependency جدید، از الگوهای موجود استفاده کنید.
- Credential یا داده‌ی واقعی پروداکشن را Commit نکنید.
- پیش از Pull Request تمام Quality Checkهای ریپو را اجرا کنید.
- تصمیم‌های معماری را در `docs/decisions/` ثبت کنید.

## مستندات

از `docs/getting-started.md` شروع کنید. راهنمای کامل‌تر توسعه‌ی AI-first در [Easy Starter Docs](https://github.com/easy-starter/easy-starter-docs) نگهداری می‌شود.

## مشارکت و پشتیبانی

قوانین مشارکت در [`CONTRIBUTING.md`](CONTRIBUTING.md)، روش دریافت کمک در [`SUPPORT.md`](SUPPORT.md) و گزارش مسائل امنیتی در [`SECURITY.md`](SECURITY.md) قرار دارد.

## مجوز

این پروژه تحت [مجوز MIT](LICENSE) منتشر می‌شود.

</div>
