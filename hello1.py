<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>動きのあるページ</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            background-color: #f0f0f0;
        }

        #animatedElement {
            width: 100px;
            height: 100px;
            background-color: #3498db;
            color: #ffffff;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: transform 0.3s ease-in-out;
        }

        #animatedElement:hover {
            transform: scale(1.1);
        }
    </style>
</head>
<body>
    <p>あ</p>
    
</body>
</html>
