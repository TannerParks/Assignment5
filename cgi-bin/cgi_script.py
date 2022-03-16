#!python

import cgi


print("Content-type: text/html \n\n")

print("""
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Leaderboards</title>
  <link rel="stylesheet" type="text/css" href="../styles.css">
</head>
<body id="form">
  <h3>Enter a username to see the leaderboard</h3>
  <h6><a href="../WebDevFinal.html">Return to main page</a></h6>
""")

data = cgi.FieldStorage()
username = data.getvalue("username", "Username not entered")

"""
This was supposed to show the table after you click the submit button and the click button
was supposed to be the score (one point for each press) but I had trouble getting the table
to stay after the button was submitted and the score didn't count up at all. I kept them in here
so you could see I tried to do a little more than just putting a name in a table even if it didn't
work out the way I wanted. 
"""

print("""
  <form method="enter" action="cgi_script.py">
    <p>Enter a username: <input type="text" name="username" autofocus/></p>
    <input id="submit" type="submit" value="submit" onclick="document.getElementById('scoreboard').style.display = 'table';">
    <input id="score" type="button" value="click" onclick="score = score + 1">


  </form>

  <table id="scoreboard">
    <tr>
      <th>User</th>
      <th>Score</th>
    </tr>
    <tr>
      <td>Joe</td>
      <td>100</td>
    </tr>
    <tr>
      <td>Bob</td>
      <td>98</td>
    </tr>
    <tr>
      <td>Kat</td>
      <td>93</td>
    </tr>
    <tr>
      <td>Brit</td>
      <td>92</td>
    </tr>
    <tr>
      <td>John</td>
      <td>89</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>{0}</td>
      <td>1</td>
    </tr>
  </table>

  <script>
    score = 0;
  </script>

</body>

</html>
""".format(username))
