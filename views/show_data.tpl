<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{database}}</title>
</head>
<body>

    <table border=1>

        <tr>
            <th>{{database}}</th>
        </tr>
        % for d in data:
        <tr>
            <td><a href='/{{database}}/{{d}}'>{{d}}</a></td>
        </tr>
        % end

    </table>

        <input position="bottom" type= 'button' onclick="location.href='/';" value='Home'>
        <input type= 'button' onclick='javascript:history.back();return false;' value='Back'>          
</html>
