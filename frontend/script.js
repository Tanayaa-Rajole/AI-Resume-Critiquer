const form = document.getElementById("resumeForm");

form.addEventListener("submit", async (event) => {

    event.preventDefault();

    const resume =
        document.getElementById("resume").files[0];

    const jobDescription =
        document.getElementById("jobDescription").value;

    const formData = new FormData();

    formData.append("resume", resume);
    formData.append(
        "job_description",
        jobDescription
    );

    document.getElementById("loading").innerText =
        "Analyzing resume...";

    try {

        const response = await fetch(
            "http://localhost:8000/api/resume/analyze",
            {
                method: "POST",
                body: formData
            }
        );

        const data = await response.json();

        document.getElementById("loading").innerText = "";

        document.getElementById("result").innerHTML = `
            <h2>Resume Analysis</h2>

            <h3>
                Section Score:
                ${data.resume_analysis.section_score}
            </h3>

            <h3>
                Keyword Match:
                ${data.keyword_analysis.match_percentage}%
            </h3>

            <h3>Missing Keywords</h3>

            <p>
                ${data.keyword_analysis.missing_keywords.join(", ")}
            </p>

            <h3>AI Feedback</h3>

            <pre>
${data.ai_analysis}
            </pre>
        `;

    } catch (error) {

        document.getElementById("loading").innerText =
            "Something went wrong.";

        console.error(error);
    }
});
