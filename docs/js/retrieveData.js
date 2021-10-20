fetch('http://localhost:8080/api/data')
    .then(res => res.json())
    .then(data => {
        document.getElementById('server-number').innerHTML = data.servers;
        document.getElementById('users-number').innerHTML = data.users;
    })
