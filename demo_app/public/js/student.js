frappe.ready(() => {
    console.log("🚀 Student Web Form Loaded!");

   
    frappe.web_form.set_value("student_name", "John Doe");

   
    let btn = document.createElement("button");
    btn.innerText = "Submit Form";
    btn.style.backgroundColor = "#42241e";
    btn.style.color = "white";
    btn.style.padding = "5px";
    btn.style.marginTop = "5px";
    btn.onclick = () => alert("Form Submitted Successfully!");

    document.querySelector(".web-form-footer").appendChild(btn);
});
