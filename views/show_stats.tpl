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
            <th>District</th>
            <th>Confirmed</th>
            <th>Active</th>
            <th>Recovered</th>
            <th>Deceased</th>
        </tr>
        % for key in data:
        <tr>
            <td>{{key['district']}} </td>
            <td>{{key['confirmed']}} </td>
            <td>{{key['active']}} </td>
            <td>{{key['recovered']}} </td>
            <td>{{key['deceased']}} </td>
        </tr>

        % end

    </table>
        <input type= 'button' onclick="location.href='/';" value='Home'>
        <input type= 'button' onclick='javascript:history.back();return false;' value='Back'>
</body>
</html>
