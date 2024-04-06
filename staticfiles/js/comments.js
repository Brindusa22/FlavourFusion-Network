const editButtons = document.querySelectorAll(".btn-edit");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

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

  for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      e.preventDefault();
      let reviewId = e.target.getAttribute("review_id");
      deleteConfirm.href = `delete_review/${reviewId}`;
      deleteModal.show();
    });
  }