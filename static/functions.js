let simp_called = false


// Function to get the sum of digits from the backend
const getSumOfDigits = () => {
    const number = document.getElementById("sumNumber").value;

    if (!simp_called) {
        document.getElementById("sumResult").innerText = 'first use simp';
        return //exit function if user didnt use simp first
    }
    axios.post('/sumofdigits', { number: parseInt(number) })
        .then(response => {
            // Display the result
            document.getElementById("sumResult").innerText = 'Sum of Digits: ' + response.data.result;
        })
        .catch(error => {
            console.error(error);
        });
}

// Function to check if a number is a palindrome using the backend
const checkPalindrome = () => {
    const number = document.getElementById("palindromeNumber").value;

    if (!simp_called) {
        document.getElementById("palindromeResult").innerText = 'first use simp';
        return //exit function if user didnt use simp first
    }

    axios.post('/ispal', { number: parseInt(number) })
        .then(response => {
            // Display the result
            document.getElementById("palindromeResult").innerText = 'Is Palindrome: ' + response.data.result;
        })
        .catch(error => {
            console.error(error);
        });
}

// Function to perform custom zip operation using the backend
const performMyZip = () => {
    const list1 = document.getElementById("zipList1").value.split(',');
    const list2 = document.getElementById("zipList2").value.split(',');
    axios.post('/myzip', { iterable1: list1, iterable2: list2 })
        .then(response => {
            // Display the result
            document.getElementById("myZipResult").innerText = 'My Zip Result: ' + JSON.stringify(response.data.result);
        })
        .catch(error => {
            console.error(error);
        });
}

// Function to perform addition using the backend
const performAddition = () => {
    const num1 = document.getElementById("addNum1").value;
    const num2 = document.getElementById("addNum2").value;
    simp_called = true

    axios.post('/add', { num1: parseInt(num1), num2: parseInt(num2) })
        .then(response => {
            // Display the result
            document.getElementById("additionResult").innerText = 'Addition Result: ' + response.data.result;
        })
        .catch(error => {
            console.error(error);
        });
}

// Function to perform subtraction using the backend
const performSubtraction = () => {
    const num1 = document.getElementById("subNum1").value;
    const num2 = document.getElementById("subNum2").value;
    simp_called = true

    axios.post('/subtract', { num1: parseInt(num1), num2: parseInt(num2) })
        .then(response => {
            // Display the result
            document.getElementById("subtractionResult").innerText = 'Subtraction Result: ' + response.data.result;
        })
        .catch(error => {
            console.error(error);
        });
}
