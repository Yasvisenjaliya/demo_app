
// $('#student-form').submit(e => {
//     e.preventDefault();
//     console.log(e.target);
    
// })


// let makecall = async () => {
//     let formdata = $('#student-form').serializeArray().reduce(
//         (obj, item) => (obj[item.name] = item.value, obj), {}
//     );
    
// }




<script>
    // Ensure jQuery is loaded
    if (typeof jQuery === "undefined") {
        console.error("jQuery is not loaded. Please include jQuery.");
} else {
        $(document).ready(function () {
            $('#student-form').submit(async function (e) {
                e.preventDefault(); // Prevent default form submission
                console.log("Form submitted:", e.target);

                let formData = new FormData(this); // Use FormData for file upload

                try {
                    let response = await fetch('/api/method/demo_app.api.upload.upload_student_file', {
                        method: 'POST',
                        body: formData,
                        headers: {
                            'X-Frappe-CSRF-Token': frappe.csrf_token // Required for Frappe API calls
                        }
                    });

                    let data = await response.json();
                    console.log("Upload Success:", data);
                } catch (error) {
                    console.error("Error:", error);
                }
            });
        });
}

</script>














// let imagefile = new FormData();
// imagefile.append('file_url', 'https://media.licdn.com/dms/image/v2/D4E12AQE9--axLTQOWg/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1684682368939?e=2147483647&v=beta&t=DGDqtpuW4IRKVGdp1W8DjJcjYPcQTzOwIe-eDEm9mO4');
// imagefile.append('doctype', 'Student');  
// imagefile.append('docname', 'STU-001'); 

// const csrfToken = document.cookie.split('; ').find(row => row.startsWith('sid='))?.split('=')[1];

// fetch('/api/method/upload_file', {
//     method: 'POST',
//     body: imagefile,
//     headers: {
//         'X-Frappe-CSRF-Token': frappe.csrf_token
  
//     }
// })
//     .then(response => response.json())
//     .then(data => {
//         console.log('Upload Success:', data);
//     })
//     .catch(error => {
//         console.error('Error:', error);
//     });
