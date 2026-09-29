# Delta for Structura Generation

## ADDED Requirements

### Requirement: Генерация ТЗ

The system SHALL возвращать структурированное ТЗ из сырого требования.

#### Scenario: Успешная генерация ТЗ
- **GIVEN** PM отправил текстовое требование
- **WHEN** Structura обрабатывает запрос
- **THEN** возвращается ТЗ с разделами: цель, scope, ограничения

### Requirement: Генерация User Story

The system SHALL возвращать User Story в формате «Как <роль>, я хочу <действие>, чтобы <ценность>».

#### Scenario: Успешная генерация User Story
- **GIVEN** PM отправил текстовое требование
- **WHEN** Structura обрабатывает запрос
- **THEN** возвращается User Story с полями role, action, value

#### Scenario: Пустой ввод
- **GIVEN** PM отправил пустую строку
- **WHEN** Structura обрабатывает запрос
- **THEN** возвращается ошибка валидации

### Requirement: Генерация Acceptance Criteria

The system SHALL возвращать AC в формате GIVEN/WHEN/THEN, покрывая основной сценарий и edge cases.

#### Scenario: Генерация AC для e-commerce
- **GIVEN** есть User Story про сопутствующие товары
- **WHEN** Structura формирует AC
- **THEN** минимум 1 AC типа main и 1 AC типа edge

### Requirement: Декомпозиция задач по ролям

The system SHALL возвращать список задач, сгруппированных по ролям: дизайнер, фронтенд, бэкенд, QA.

#### Scenario: Задачи для всех ролей
- **GIVEN** есть ТЗ и Acceptance Criteria
- **WHEN** Structura формирует задачи
- **THEN** каждая роль получает минимум 1 задачу с описанием и Story Points

#### Scenario: Задачи только для затронутых ролей
- **GIVEN** требование не затрагивает дизайн
- **WHEN** Structura формирует задачи
- **THEN** задачи для дизайнера отсутствуют или помечены как optional

### Requirement: Генерация тест-кейсов

The system SHALL возвращать тест-кейсы на pytest на основе Acceptance Criteria.

#### Scenario: Тест-кейсы покрывают все AC
- **GIVEN** есть AC-1, AC-2, AC-3
- **WHEN** Structura генерирует тесты
- **THEN** каждый AC покрыт минимум одним тестом с ссылкой на ac_id

#### Scenario: Тесты запускаются без доработки
- **GIVEN** сгенерированные тесты скопированы в проект
- **WHEN** запускается pytest
- **THEN** тесты выполняются без синтаксических ошибок

### Requirement: Валидация контракта вывода

The system SHALL валидировать вывод через Pydantic-схему StructuraOutput.

#### Scenario: Невалидный вывод от LLM
- **GIVEN** LLM вернул JSON без поля user_story
- **WHEN** Structura валидирует результат
- **THEN** генерация помечается как failed с указанием ошибки