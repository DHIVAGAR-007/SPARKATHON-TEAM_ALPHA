async function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const userType = document.getElementById('userType').value;

    let formData = new FormData();
    formData.append("username", username);
    formData.append("password", password);

    let response = await fetch("http://127.0.0.1:8000/login", {
        method: "POST",
        body: formData
    });

    let data = await response.json();

    if (!data.success) {
        alert(data.message);
        return;
    }

    currentUser = { username, role: data.role };
    document.getElementById('authSection').style.display = 'none';
    document.getElementById('dashboard').classList.add('active');
    document.getElementById('welcomeMessage').textContent = `Welcome, ${username}!`;
    document.getElementById('userRole').textContent = `Role: ${data.role}`;

    if (userType === 'department' || userType === 'faculty') {
        document.getElementById('uploadSection').style.display = 'block';
    }

    loadReports();
}
