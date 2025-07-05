document.getElementById("careerForm").addEventListener("submit", function(e) {
  e.preventDefault();

  const interests = Array.from(document.querySelectorAll('input[name="interest"]:checked')).map(el => el.value);
  const subject = document.getElementById("subject").value;
  const personality = document.getElementById("personality").value;

  let suggestions = [];

  if (interests.includes("Tech") && subject === "Computer") {
    suggestions.push("Software Engineer", "Web Developer", "AI Engineer");
  }
  if (interests.includes("Art") && personality === "Creative") {
    suggestions.push("Graphic Designer", "Animator", "UI/UX Designer");
  }
  if (interests.includes("Science") && subject === "Biology") {
    suggestions.push("Doctor", "Biologist", "Lab Technician");
  }
  if (interests.includes("Business") && (personality === "Leader" || personality === "Creative")) {
    suggestions.push("Entrepreneur", "Marketing Manager", "Business Analyst");
  }
  if (interests.includes("Health") && personality === "Helpful") {
    suggestions.push("Nurse", "Psychologist", "Nutritionist");
  }

  const resultBox = document.getElementById("result");
  resultBox.style.display = "block";

  if (suggestions.length === 0) {
    resultBox.innerHTML = "<b>No matching careers found. Try selecting different options.</b>";
  } else {
   resultBox.innerHTML = `<b>Top Career Matches:</b><ul>${suggestions.map(s => `<li>${s}</li>`).join('')}</ul>`;
  }
});