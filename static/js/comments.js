const editButtons = document.querySelectorAll(".btn-edit");

  editButtons.forEach(button => {
    button.addEventListener("click", () => {
        const reviewId = button.getAttribute("data-review-id");
        const editForm = document.getElementById(`editForm_${reviewId}`);
        if (editForm.style.display === "none") {
            editForm.style.display = "block";
        } else {
          editForm.style.display = "none";
        }
    });
  });