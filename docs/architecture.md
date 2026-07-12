# Architecture
Version: 0.1

Status: Draft

Author: Project Team

---

## Mission

Создать систему визуального анализа фотографий, способную принимать решения на уровне арт-директора.

Система не должна быть привязана к Instagram.

Instagram является только одним из вариантов применения.

---

## Principles

### 1. Domain First

Архитектура строится вокруг предметной области.

Не вокруг технологий.

Не вокруг библиотек.

Не вокруг моделей AI.

---

### 2. Explainability

Каждое решение должно иметь объяснение.

Система никогда не должна возвращать только число.

Любая рекомендация должна сопровождаться причиной.

---

### 3. Replaceable AI

Любая модель может быть заменена.

Ни один модуль системы не должен зависеть от конкретной модели.

Например:

Сегодня

CLIP

Завтра

Florence

После завтра

GPT Vision

Архитектура остается неизменной.

---

### 4. Independent Modules

Каждый модуль отвечает только за свою задачу.

Vision Engine

не знает

что такое Instagram.

Layout Engine

не знает

как работает анализ изображения.

Recommendation Engine

не знает

как извлекаются признаки.

---

### 5. Human Override

Любое решение AI может быть изменено человеком.

Система предлагает.

Человек принимает решение.

---

## Architecture

Browser

↓

Frontend

↓

API

↓

Vision Engine

↓

Feature Database

↓

Layout Engine

↓

Recommendation Engine

↓

Export

---

## Long-term Goals

- Instagram

- Portfolio

- Exhibition

- Book

- Storytelling

- Client Presentation

- Personal Archive
