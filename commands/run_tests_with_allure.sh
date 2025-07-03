#!/bin/bash

ROOT_DIR="$(dirname "$0")"  # путь до текущего .sh-файла
ALLURE_DIR="$ROOT_DIR/allure-results"

mkdir -p "$ALLURE_DIR"  # Создать папку, если её нет

pytest tests/ --alluredir="$ALLURE_DIR"

allure serve "$ALLURE_DIR"
