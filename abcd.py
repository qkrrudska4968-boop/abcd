<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>간단 계산기</title>
    <style>
        /* CSS: 디자인 */
        .calculator {
            width: 300px;
            margin: 50px auto;
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            background-color: #f9f9f9;
        }
        #display {
            width: 95%;
            height: 50px;
            margin-bottom: 10px;
            padding: 10px;
            font-size: 2em;
            text-align: right;
            border: 1px solid #aaa;
            border-radius: 5px;
            background-color: #fff;
        }
        .buttons {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
        }
        button {
            padding: 20px;
            font-size: 1.2em;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            background-color: #e0e0e0;
        }
        button:hover {
            background-color: #d0d0d0;
        }
        .operator {
            background-color: #ff9500;
            color: white;
        }
        .operator:hover {
            background-color: #e08b00;
        }
        .clear {
            background-color: #ff3b30;
            color: white;
        }
        .clear:hover {
            background-color: #e03028;
        }
        .equals {
            background-color: #4cd964;
            color: white;
            grid-column: span 1; /* '=' 버튼을 한 칸만 차지하도록 설정 */
        }
        .equals:hover {
            background-color: #40c056;
        }
        .span-2 {
            grid-column: span 2; /* '0' 버튼을 두 칸 차지하도록 설정 */
        }
    </style>
</head>
<body>

<div class="calculator">
    <input type="text" id="display" disabled value="0">
    
    <div class="buttons">
        <button class="clear span-2" onclick="clearDisplay()">AC</button>
        <button class="operator" onclick="appendOperator('/')">/</button>
        <button class="operator" onclick="appendOperator('*')">*</button>
        
        <button onclick="appendNumber(7)">7</button>
        <button onclick="appendNumber(8)">8</button>
        <button onclick="appendNumber(9)">9</button>
        <button class="operator" onclick="appendOperator('-')">-</button>
        
        <button onclick="appendNumber(4)">4</button>
        <button onclick="appendNumber(5)">5</button>
        <button onclick="appendNumber(6)">6</button>
        <button class="operator" onclick="appendOperator('+')">+</button>
        
        <button onclick="appendNumber(1)">1</button>
        <button onclick="appendNumber(2)">2</button>
        <button onclick="appendNumber(3)">3</button>
        <button class="equals" onclick="calculate()">=</button>

        <button class="span-2" onclick="appendNumber(0)">0</button>
        <button onclick="appendNumber('.')">.</button>
    </div>
</div>

<script>
    // JavaScript: 계산 로직
    const display = document.getElementById('display');
    let currentInput = '0';
    let previousInput = null;
    let operator = null;

    function updateDisplay(value) {
        display.value = value;
    }

    // 숫자 버튼 클릭 시
    function appendNumber(number) {
        if (currentInput === '0' && number !== '.') {
            currentInput = String(number);
        } else if (number === '.' && currentInput.includes('.')) {
            return; // 이미 소수점이 있으면 무시
        } else {
            currentInput += String(number);
        }
        updateDisplay(currentInput);
    }

    // 연산자 버튼 클릭 시
    function appendOperator(op) {
        if (previousInput !== null && operator !== null) {
            calculate(); // 연산자가 이미 있으면 중간 계산 실행
        }
        previousInput = parseFloat(currentInput); // 현재 값을 첫 번째 숫자로 저장
        operator = op; // 연산자 저장
        currentInput = '0'; // 다음 숫자 입력을 위해 초기화
        updateDisplay(previousInput + ' ' + operator); // 중간 상태 표시
    }

    // 초기화 버튼 클릭 시 (AC)
    function clearDisplay() {
        currentInput = '0';
        previousInput = null;
        operator = null;
        updateDisplay(currentInput);
    }

    // 계산 버튼 클릭 시 (=)
    function calculate() {
        if (previousInput === null || operator === null) return;

        const secondNum = parseFloat(currentInput);
        let result;

        switch (operator) {
            case '+':
                result = previousInput + secondNum;
                break;
            case '-':
                result = previousInput - secondNum;
                break;
            case '*':
                result = previousInput * secondNum;
                break;
            case '/':
                // 0으로 나누는 경우 처리
                if (secondNum === 0) {
                    result = 'Error';
                } else {
                    result = previousInput / secondNum;
                }
                break;
            default:
                return;
        }

        // 결과 업데이트 및 상태 초기화
        currentInput = String(result);
        previousInput = null;
        operator = null;
        updateDisplay(currentInput);
    }

    // 초기 로드 시 디스플레이 설정
    updateDisplay(currentInput);
</script>
</body>
</html>
