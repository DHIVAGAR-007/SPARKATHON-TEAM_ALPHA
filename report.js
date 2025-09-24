async function uploadFiles() {
    const fileInput = document.getElementById('reportFile');
    if (fileInput.files.length === 0) return;

    let formData = new FormData();
    formData.append("dept", currentUser.username + " Department");
    formData.append("title", "New Annual Report 2024");
    formData.append("file", fileInput.files[0]);

    let response = await fetch("http://127.0.0.1:8000/upload-report", {
        method: "POST",
        body: formData
    });

    let data = await response.json();
    alert(data.message);

    loadReports();
    fileInput.value = '';
    document.getElementById('fileList').innerHTML = '';
}
