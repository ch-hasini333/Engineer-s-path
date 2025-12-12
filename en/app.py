import os
from flask import Flask, render_template, request, jsonify
# NOTE: The 'google' package needs to be installed (pip install google-genai)
from google import genai 

# --- Flask Setup ---
# Initialize Flask app
app = Flask(__name__)

# Configure the Gemini API client (ensure GEMINI_API_KEY is set in your environment)
# IMPORTANT: You must set the GEMINI_API_KEY environment variable for this to work.
try:
    client = genai.Client()
except Exception as e:
    print(f"Warning: Could not initialize Gemini Client. API calls will fail. Error: {e}")

# --- 1. Career Content Data (Detailed and Comprehensive, includes Curriculum) ---
# Data is structured as a list of dictionaries. Each dictionary represents a single topic card.
CONTENT_DATA = [
    {
        "heading": "🚀 Career Roadmap & Pipeline",
        "importance": "Crucial for guiding academic choices and skill development. It defines the path from college to career.",
        "content": """⭐ What is a Roadmap?

A roadmap is a high-level plan that shows the direction, goals, and timeline of a project, product, or learning journey.
It tells what will happen, when it will happen, and why it is important.

🔹 Purpose of a Roadmap

To show the big-picture plan

To communicate the future vision

To guide teams on what to build or learn next

To keep everyone moving in the same direction

🔹 Example (Engineering Student Roadmap)

Year 1 → Basics
Learn maths, physics, programming basics.

Year 2 → Core subjects
Learn electronics, circuits, algorithms.

Year 3 → Skills
Do internships, projects, build resume.

Year 4 → Placement
Prepare for interviews, GATE, higher studies.

👉 This is a roadmap because it shows overall direction and milestones, not small tasks.

⭐ What is a Pipeline?

A pipeline is a step-by-step process that takes an input, processes it through stages, and produces an output.

It shows how work flows.

🔹 Purpose of a Pipeline

To define the exact sequence of steps

To automate or standardize repeatable tasks

To ensure everything moves smoothly from start → end

To show how data, code, or tasks are processed

🔹 Example (Machine Learning Pipeline)

Collect data

Clean the data

Split into train/test

Train the model

Evaluate

Deploy

👉 This is a pipeline because it shows how the work flows, step-by-step.
⭐ Very Simple Memory Trick

Roadmap = Future direction
Pipeline = Current workflow """,
        "link": "https://www.geeksforgeeks.org/full-stack-developer-roadmap/"
    },
    {
        "heading": "💰 Education Loan for Laptops/Expenses",
        "importance": "Helps manage finances and ensure you acquire necessary, high-specification equipment without burdening family immediately.",
        "content": """Purpose in Engineering Context

Banks provide laptop loans because:

Engineers need high-performance systems for computational workloads.

Coursework often requires software licensing, development environments, and project execution.

A laptop directly contributes to academic performance, internships, and capstone projects.

So it is treated like books, exam fees, or lab equipment. Two Ways to Get a Laptop Loan
A) Education Loan (General)

If you already have an education loan for B.Tech/Diploma, you can add laptop cost under:
✔ “Equipment required for the course”
✔ Usually up to ₹40,000–₹1,00,000 for laptops

B) Dedicated Laptop/Gadget Loan

Some banks/NBFCs give separate loans just for electronics:
✔ 0% interest EMI (online stores)
✔ Quick approval
✔ No big documents
✔ ₹25,000 – ₹1,50,000 range.Eligibility

Must be a student in Diploma/B.Tech/M.Tech

Laptop cost must directly support academic work

Parent/guardian should have a regular income (for EMI repayment)

Age usually 18+ (if below, parent signs). Documents Required (Engineering Student View)

College ID Card

Admission letter (proof you are an active student)

Laptop quotation from store/online (like HP, Lenovo, Flipkart)

Aadhaar + PAN

Parent/guardian income proof (salary slip / ITR)

Bank statements (last 6 months)""",
        
    },
    {
        "heading": "👔 LinkedIn, Resume & ATS",
        "importance": "These are your primary marketing tools. A poor resume will be filtered out by software (ATS) before a human sees it.",
        "content": """LinkedIn is a professional engineering network, just like a digital ecosystem where:

Engineers connect with companies

Students show their projects

Recruiters discover skilled candidates

Professionals share technical ideas

Think of it like a network topology where every node = a person/company, and connections = communication channels. 🛠️ Why Engineers MUST use LinkedIn

Engineering students get huge benefits:

1. Internships & Job Opportunities

Companies post:

Internships (Amazon, TCS, Infosys, Bosch)

Entry-level roles

Campus hiring programs

You can apply directly without waiting for college placements. 1. Show Your Engineering Projects

Your LinkedIn profile becomes a digital portfolio.
You can upload:

IoT projects

Coding mini-projects

MATLAB simulations

Arduino/ESP32 prototypes

Civil/Mechanical CAD designs

Research papers

Recruiters judge engineers mainly by projects, skills, certifications. 2. Networking = Direct access to industry experts

You can connect with:

Senior engineers

CTOs, CEOs

HR recruiters

College alumni working in top companies

This is like building a strong wireless network — greater range = more opportunities. 3. Skill Visibility & Certifications

You can add certifications from:

Coursera

NPTEL

Udemy

Cisco

Microsoft

This increases your profile strength (like increasing signal strength). 4. Engineering Content Learning

Many engineers share:

Coding tips

Project ideas

Career guidance

Placement preparation

Industry trends (AI, IoT, EV, VLSI, Robotics)

Your feed becomes a knowledge pipeline. 🔥 Why Recruiters Check LinkedIn First

Because it shows:

Real skills → what you actually know

Project execution capability

Consistency in learning

Technical communication

Professional behaviour

Companies prefer students who have documented engineering growth. ⭐ What is a Resume? (Engineering Perspective)

A resume is a structured technical document that represents an engineer’s skills, academic qualifications, project experience, certifications, tools used, and achievements. It works like a specification sheet (spec sheet) of an engineering component. Just as every device has a datasheet that tells how it performs, your resume acts as your personal datasheet that tells recruiters what you can do. It must clearly show your core strengths, such as programming languages, engineering tools, domain knowledge, and the ability to solve real-world problems. A strong resume makes it easy for companies to understand your capabilities in a quick scan of 6–10 seconds, which is usually the time a recruiter spends on each application. For engineering students, a resume becomes the first proof of your technical identity, showcasing academic projects, mini-projects, internships, and problem-solving skills. It is not just a document—it is your first impression, entry pass, and professional signature. ⭐ What is ATS? (Applicant Tracking System — Engineering Explanation)

An ATS, or Applicant Tracking System, is a software pipeline that companies use to automatically filter thousands of resumes. Think of it like a compiler or pre-processing tool that checks your resume before a human sees it. Just as a compiler rejects code with errors or missing syntax, ATS rejects resumes that do not follow proper formatting, keywords, and structure. The system scans for engineering keywords like Python, Java, AutoCAD, MATLAB, IoT, Embedded Systems, Data Structures, or any skill listed in the job description. If these keywords do not appear in your resume, the ATS may give a low score and filter you out before a recruiter even opens your file. Many resumes get rejected not because the candidate is weak, but because the resume is not ATS-friendly. This makes ATS optimization a technical requirement, similar to optimizing algorithms for better performance. ⭐ Why ATS Matters for Engineering Students

Most engineering jobs, internships, and campus placements use an ATS to handle large volumes of applicants. For example, big companies like TCS, Infosys, Amazon, Qualcomm, L&T, or Siemens receive thousands of engineering applications in a single week. Without ATS, recruiters cannot manually check every resume. Therefore, your resume must be built using simple formatting, correct headings, consistent fonts, and job-relevant keywords. Images, tables, fancy designs, and multiple columns confuse ATS, just like noisy data confuses a machine learning model. When your resume is ATS-compliant, it passes through the automated filtration pipeline and reaches the recruiter. If not, it gets rejected automatically—even if you are a very strong engineering student. That's why an engineering resume must be technically clean, keyword-rich, and machine-readable. ⭐ Key Connection Between Resume & ATS (Engineering Analogy)

Think of the resume as the input file and ATS as the processing system.

If the input file has correct syntax (layout), right variables (keywords), and readable formatting, the processing completes successfully, and the output is positive (resume forwarded).

If the resume has errors, images, wrong formats, or missing job-related keywords, the system rejects it during pre-processing—just like a compiler rejecting faulty code.""",
        "link": "https://www.linkedin.com/"
    },
    {
        "heading": "💻 Projects & SDLC",
        "importance": "Demonstrates practical application of theoretical knowledge, essential for interviews and professional team work.",
        "content": """⭐ How Many Projects Should an Engineering Student Do by Final Year?

By the time an engineering student reaches final year, an ideal profile should include 3–6 projects, depending on the branch and depth. Generally, students complete at least one project per year, starting from basic models in first year to advanced, domain-specific systems in final year. In early years, projects focus on understanding fundamentals—simple circuits, basic coding tasks, IoT prototypes, database systems, mini MATLAB simulations, structural models, or mechanical designs. By second or third year, projects become more application-oriented, integrating multiple subjects like microcontrollers, embedded systems, AI/ML, web development, networking labs, VLSI basics, or CAD designs. In final year, students are expected to deliver one major capstone project, which shows their engineering maturity, problem-solving ability, teamwork, system design capability, and readiness for industry. Recruiters treat projects as validation that the student has applied engineering concepts in real-world conditions. So more projects = stronger engineering portfolio = higher chances of internship, job, or higher studies. ⭐ Why Do Engineering Students Do Projects? (Purpose & Benefits)

Projects are not just assignments—they are proof of engineering thinking. Engineering is fundamentally about solving real-world problems using scientific principles and technology. Projects convert theoretical knowledge (from textbooks and labs) into practical, implementable systems. They help students learn how to identify a problem, analyze requirements, design a solution, integrate hardware/software, test performance, debug issues, and finally deploy the system. This hands-on process teaches critical skills like teamwork, documentation, system integration, version control, troubleshooting, optimization, and presenting solutions to evaluators. Projects also showcase a student’s technical identity—whether they are strong in embedded systems, IoT, software development, civil planning, mechanical design, VLSI, robotics, or networking. That’s why companies value projects more than marks; a student with strong projects is seen as “industry-ready.” Projects prepare students for internships, build vision for innovation, and help them understand real engineering workflows. ⭐ Importance of SDLC (Software Development Life Cycle) in Engineering

SDLC is crucial because it defines how engineering projects should be planned, designed, developed, tested, and deployed in a structured and reliable way. Without a proper life cycle, projects become chaotic—requirements get misunderstood, development takes longer, quality drops, debugging becomes difficult, and the final system may not work as expected. SDLC acts like a blueprint or engineering manufacturing process, ensuring every phase is completed with clarity.

In engineering terms, SDLC provides:

Requirement Analysis: Understanding the real problem, constraints, user needs

System Design: Designing architecture, UML diagrams, data flow, hardware selection

Implementation: Writing clean, modular, maintainable code or assembling hardware

Testing: Identifying bugs, performance problems, edge cases

Deployment: Delivering the working version to the end user

Maintenance: Updating features, fixing issues, improving efficiency

This life cycle ensures that the final software or system is reliable, scalable, secure, and maintainable. In real industries—software companies, embedded systems teams, automation, IoT manufacturing—projects strictly follow SDLC to avoid failure. Thus, understanding SDLC makes engineering students ready for professional engineering workflows and industry work culture. ⭐ Simple Engineering Summary

3–6 projects (mini + major) make an engineer industry-ready.

Projects teach real problem-solving, not just theory.

SDLC ensures projects are built systematically, reducing errors and improving quality. """,
    },
    {
        "heading": "🧠 DSA for High-Paying Jobs",
        "importance": "A prerequisite for cracking interviews at top product-based MNCs and high-growth startups.",
        "content": """ ⭐ Why DSA Is Important for High-Paying Engineering Jobs

In the engineering and software industry, companies design systems that must process massive amounts of data with maximum efficiency. A high-paying engineer is not hired to just “write code” — anyone can do that. They are hired to build optimized, scalable, and high-performance systems. This is where Data Structures and Algorithms (DSA) become the core foundation. DSA teaches how to organize data (using structures like arrays, stacks, trees, graphs, heaps) and how to process that data efficiently (using searching, sorting, recursion, dynamic programming, greedy approaches, etc.). These are the exact skills needed to build real-world systems like compilers, recommendation engines, OS-level schedulers, databases, networking protocols, IoT firmware, cloud architectures, and high-load applications. Companies pay higher salaries to engineers who can design these kinds of optimized systems—not just write basic programs. ⭐ How DSA Directly Connects to High-Paying Job Roles (Engineering View)

Top companies like Google, Amazon, Microsoft, Meta, Adobe, and high-tech startups handle millions of users, terabytes of data, and real-time operations. Even a small inefficiency in the system can cause millions of rupees loss. Therefore, they need engineers who deeply understand:

How to reduce time complexity (O(n) → O(log n))

How to reduce space usage

How to design algorithms that scale

How to handle worst-case scenarios

How to optimize live systems during peak loads

DSA proves whether an engineer can build intelligent, efficient solutions instead of brute-force code. High-paying jobs require this skill because performance, reliability, and optimization are the backbone of world-class engineering. ⭐ DSA Improves an Engineer’s Problem-Solving Mindset

Engineering is all about solving problems under constraints — limited memory, limited time, limited CPU, or limited resources. DSA shapes your brain to think like an algorithmic engineer. It teaches you how to break a complex problem into smaller modules, identify edge cases, design optimal approaches, and ensure correctness. This thought process is the same whether you are designing a robot’s path planning system, building a microcontroller control loop, optimizing a network protocol, or writing backend APIs. Companies pay more to engineers who think in a logical, structured, and optimized way — DSA trains exactly that mindset. ⭐ Why Interviews Focus So Much on DSA

Top companies cannot test you on every technology (Java, Python, React, AWS, IoT, ML...). Instead, they test the one skill that proves your raw engineering ability:
Your capability to solve unseen problems using logic, data flow, structures, and algorithms.
If you can solve tough DSA problems, companies know you can learn any technology quickly. That is why most high-paying jobs include multiple rounds of coding challenges, system design, and algorithmic problem-solving. These tests filter out candidates who only know basic programming and select engineers who possess deep computational thinking. ⭐ Simple Engineering Summary

High-paying companies handle huge data → they need optimized solutions.

DSA proves your ability to think logically and solve problems efficiently.

Strong DSA = strong engineering foundation → higher salary.

DSA skills allow you to crack the toughest interviews and design scalable systems. """,
        "link": "https://www.geeksforgeeks.org/data-structures/"
    },
    {
        "heading": "🎓 M.Tech / GATE & Naukari",
        "importance": """Pursuing MTech through GATE is one of the strongest academic paths for engineering students who want deeper technical expertise, core-sector careers, or research opportunities. The GATE exam (Graduate Aptitude Test in Engineering) evaluates your understanding of engineering fundamentals, problem-solving accuracy, and analytical skills. A good GATE score opens admission to top institutions like IITs, NITs, IIITs, where MTech programs allow you to work on advanced domains such as embedded systems, VLSI, IoT, AI, machine learning, robotics, cybersecurity, renewable energy systems, and structural engineering. During MTech, you get access to specialized labs, funded research projects, internships, and high-level professors, which strengthens your engineering depth compared to a normal BTech path. It also increases your chances of high-paying PSUs (like ONGC, BHEL, IOCL, NTPC, DRDO, ISRO) because many government organizations shortlist candidates directly based on GATE rank. MTech graduates also have better opportunities for R&D roles, teaching careers, and PhD pathways. Most importantly, preparing for GATE improves your core engineering logic, making you technically stronger and more competitive in both academia and industry. Naukri.com is India’s largest online job portal used by engineering graduates to search and apply for technical and non-technical roles across IT, core engineering, government-linked companies, and startups. The platform works as a career marketplace, where your uploaded resume is scanned by recruiters using ATS (Applicant Tracking Systems) to match skills, keywords, and project experience. For engineering students, Naukri is useful because it provides personalized job recommendations, filters based on skills like Python, Java, IoT, Embedded Systems, Data Science, Civil/Mechanical domains, and alerts for freshers hiring, internships, walk-ins, and off-campus drives. Recruiters from top companies use Naukri to directly reach out when your profile matches their project needs, so maintaining a technically strong resume, clear project descriptions, and relevant certifications increases your visibility. Naukri also offers features like resume score, company reviews, salary insights, and skill tests, which help engineering students plan their career path scientifically. Overall, it acts as a bridge between your engineering skillset and industry requirements, improving chances of getting interviews and high-quality job opportunities. """,
    },
    {
        "heading": "🌐 LeetCode, HackerRank, & Resources",
        "importance": """ LeetCode

LeetCode is a global coding practice platform designed mainly for Data Structures & Algorithms (DSA) and technical interview preparation, especially for high‑paying software engineering roles. It focuses on problem‑solving efficiency, requiring engineers to write optimized solutions based on time and space complexity. Companies like Google, Amazon, Microsoft, and Adobe directly use LeetCode‑style questions in interviews, so solving these problems builds strong analytical and algorithmic thinking. The platform also provides editorials, discussion forums, and contest challenges, which help engineering graduates understand multiple solution approaches and benchmark their performance against global programmers. HackerRank

HackerRank is a structured programming and skill‑assessment platform widely used by companies to conduct online coding tests, 30‑minute skill assessments, MCQs, and technical screenings. It supports multiple engineering domains like C/C++, Python, Java, SQL, Linux, AI, and problem‑solving fundamentals. Many companies send direct HackerRank tests for hiring, making the platform essential for freshers preparing for campus placements. HackerRank tracks your progress with badges, ranks, and leaderboards, which helps in building a technical profile and demonstrating your core engineering skills. Useful Resources for Engineering Students

Engineering students preparing for software roles can rely on a combination of structured and self-learning resources. Platforms like GeeksforGeeks (GfG) provide deep explanations, interview experiences, MCQs, and complete DSA roadmaps. YouTube channels such as Kunal Kushwaha, CodeWithHarry, Jenny’s Lectures, and Neso Academy help in understanding concepts from scratch. If you want project‑based learning, free resources like Google Cloud Skills Boost, GitHub, Kaggle, Coursera (free audit), and MIT OpenCourseWare can build strong hands‑on experience. In addition, using ChatGPT as a code explainer, taking notes in Notion, and practicing Git/GitHub ensure that you learn engineering concepts in a structured, SDLC‑oriented way.""",
        "link": "https://leetcode.com/"
    },
    {
        "heading": "📝 Aptitude, Reasoning, & Indiabix",
        "importance": """Aptitude in Engineering Careers

Aptitude is a core skill for engineering students because it evaluates your problem-solving ability, quantitative reasoning, and logical thinking, which are crucial for both campus placements and competitive exams. Questions typically include numbers, percentages, ratios, algebra, probability, time-speed-distance, work & time, and other quantitative problems. Strong aptitude skills reflect an engineer’s ability to analyze complex scenarios quickly, optimize solutions, and handle calculations efficiently—qualities highly valued in roles like software development, data analysis, design engineering, and embedded systems. Many companies, especially IT and consulting firms, use aptitude tests as a first-stage screening before technical interviews. Reasoning in Engineering Context

Reasoning tests evaluate your analytical and logical thinking, which is critical for engineers working in problem-solving domains such as algorithms, coding, electronics troubleshooting, network design, and mechanical systems optimization. It includes logical puzzles, series, analogies, coding-decoding, syllogisms, seating arrangements, and flowcharts. These exercises train engineers to identify patterns, understand dependencies, and make accurate decisions under time pressure, which directly correlates with system design, debugging, and optimization tasks in real engineering projects. IndiaBix App – A Resource for Aptitude and Reasoning

The IndiaBix app is a dedicated platform for practicing quantitative aptitude, reasoning, and verbal skills for engineering students preparing for placement exams, competitive exams, or government jobs. It offers a huge question bank with solutions, shortcuts, and tricks, making it easier for students to practice daily and track improvement. Engineers can use the app to simulate test environments similar to campus recruitment or online coding aptitude tests, which helps in time management, speed optimization, and accuracy. IndiaBix also provides topic-wise tutorials, making it a valuable resource for building strong fundamentals in both numerical and logical problem solving, bridging the gap between academic learning and placement requirements. """,
        "link": "https://www.indiabix.com/"
    },
    {
        "heading": "🏢 Company Types (Startup, Mid, MNC)",
        "importance": """ 1. MNCs (Multinational Corporations)

MNCs are large, well-established companies that operate globally, such as Google, Microsoft, Amazon, Infosys, TCS, Siemens, Bosch. These companies generally have structured hiring processes, well-defined job roles, and standardized pay scales. For engineers, working in an MNC provides:

Stability: fixed salary, bonuses, provident fund, insurance, and allowances.

Structured growth: clear promotions and appraisal cycles.

High exposure: international projects, diverse technologies, professional training programs.

Salary range for fresh engineering graduates:

IT/software MNCs: ₹5–15 LPA depending on the company and role (product-based companies like Google/Amazon pay on the higher side).

Core MNCs (mechanical, civil, electrical): ₹3–8 LPA, depending on profile and location.

MNCs are ideal for engineers seeking long-term career stability, learning from senior professionals, and gradual growth. 2. Mid-Sized Companies

Mid-sized companies are regional or national firms with 50–5000 employees, such as Zoho, Freshworks, Mindtree, L&T Construction, ABB India. They usually offer:

Moderate salary packages: slightly lower than MNCs but often competitive.

Broader responsibilities: engineers often handle multiple roles like design, testing, and deployment.

Faster recognition: your work is more visible, giving early career exposure.

Salary range for freshers:

₹3–8 LPA for software and IT engineers

₹2.5–6 LPA for core engineering roles

Mid-sized companies are suitable for engineers looking for hands-on experience and faster growth, especially in smaller teams where work visibility is high. 3. Startups

Startups are small, early-stage companies, typically with 10–500 employees, focusing on new products or disruptive technologies. Examples include Ola, Razorpay, Unacademy, FreshToHome. Startups have:

Variable salaries: Early-stage startups may pay ₹2–5 LPA, while funded startups may offer ₹6–12 LPA with stock options (ESOPs).

High learning curve: Engineers often do full-stack work, taking ownership of multiple modules or processes.

Growth opportunities: Rapid promotions if the startup succeeds; sometimes employees become team leads within 1–2 years.

Risk factor: If funding fails, job security is low.

Startups are ideal for engineers who want exposure to emerging technologies, entrepreneurship mindset, and fast-tracked responsibilities. """,
           },
    {
        "heading": "🤝 Internships & Types",
        "importance": """ Why Internships Are Important for Engineering Students

Internships are a critical part of engineering education because they provide practical, hands-on experience that bridges the gap between academic learning and real-world industry applications. While classroom subjects teach concepts, formulas, and theoretical design principles, internships let students apply these principles on live projects, understand workflow processes, use professional tools, collaborate with cross-functional teams, and experience workplace culture. For example, a mechanical engineering student may learn about thermodynamics in class, but during an internship at a manufacturing plant, they see real machines, CNC operations, or CAD-based design processes. Similarly, a computer science student may implement AI, full-stack development, or database projects in an internship, understanding how code interacts in a production environment. Internships also help students develop problem-solving skills, time management, teamwork, and communication, which are highly valued by recruiters. Moreover, successful internships enhance a student’s resume, improve their chances of pre-placement offers (PPOs), and can even guide career specialization choices by exposing them to different domains. Types of Internships for Engineering Students

Engineering internships can be broadly categorized into several types depending on the mode, domain, and industry exposure:

Technical Internships – Focused on domain-specific engineering work, such as software development, IoT projects, VLSI design, robotics, embedded systems, civil project planning, or mechanical CAD design. These are the most common for final-year students aiming for core roles.

Research Internships – Usually offered by IITs, NITs, DRDO, ISRO, or research labs, where students work on experimental projects, simulations, algorithm development, or prototype design. These enhance analytical thinking and can lead to MTech/PhD opportunities.

Industrial/Corporate Internships – Conducted in manufacturing, construction, energy, IT services, or consulting companies, focusing on real production systems, quality control, process optimization, or project management. These give exposure to practical industrial workflow.

Virtual/Online Internships – Increasingly popular due to remote opportunities. Students work on coding projects, simulations, data analysis, or AI/ML models without visiting the office. Tools like GitHub, Google Colab, MATLAB, and Zoom are used for collaboration.

Startup Internships – Involve working in early-stage startups, where engineers often handle multiple responsibilities such as design, coding, testing, and deployment. These internships are highly dynamic and provide a fast learning curve.

Non-Technical/Soft-Skill Internships – Some students also take internships in project management, technical documentation, product design, or marketing of engineering products, which help improve communication, reporting, and managerial skills alongside technical knowledge.

Engineering Perspective Summary

Internships are not optional; they are core for career development in engineering. They let students apply concepts, gain exposure to professional tools, interact with real systems, and understand industry standards. Ideally, an engineering student should aim for 2–3 internships: one basic or domain-exploratory internship in early years and one or two specialized, final-year internships aligned with their target career path. These experiences significantly increase employability, prepare students for high-paying jobs, core roles, or research positions, and build a strong engineering portfolio. """,
        
    },
    {
        "heading": "🧑‍💻 AI Tools (Gemini, Copilot, Gamma)",
        "importance": """ Google Gemini

Google Gemini is a powerful general‑purpose AI assistant developed by Google. It combines natural language understanding and generation to help with a wide range of tasks — from research and problem solving to code generation and content creation. Unlike traditional chatbots, Gemini can handle long context windows, meaning it can understand and generate responses even when you give it large chunks of text or complex prompts, which is especially helpful when you’re working on engineering documentation, research summaries, or coding tasks. It can also integrate with tools like command‑line interfaces for development workflows, allowing engineers to generate code, debug, and manage tasks through natural language prompts in the terminal. Perplexity AI

Perplexity AI is an AI‑powered search and research assistant that blends a search engine with generative AI. Instead of just returning a list of links like Google, Perplexity reads and synthesizes information from the web in response to your query, and summarizes the results in clear answers — which is extremely useful when you’re conducting technical research, gathering facts for reports, or preparing engineering presentations. It offers modes for quick search and detailed research, allowing engineers to switch between concise summaries and in‑depth explanations. Features like web page creation and browser tools extend its capabilities beyond basic search, making it an efficient information pipeline for study and project work. Gamma

Gamma is an AI‑powered presentation and content design tool that helps you instantly generate professional slide decks, documents, and even webpage‑style presentations from simple text prompts. Instead of manually designing slides in PowerPoint or Google Slides, you describe your topic and Gamma generates polished, responsive presentations with layouts, text flows, and visual elements integrated. This is incredibly helpful for final‑year project defense slides, seminar presentations, proposal documents, and quick concept visualizations for engineering projects — saving time and enhancing clarity without needing deep design skills. Many students and professionals use it as a modern alternative to traditional slide software because of its speed and ease of use. GitHub Copilot

GitHub Copilot is an AI pair programmer built into popular coding environments like Visual Studio Code, Visual Studio, and JetBrains IDEs. It’s designed to autocomplete code, generate functions, suggest logic, and even write larger blocks of code based on natural language comments or partial code patterns. For engineering students and developers, Copilot accelerates coding tasks, helps explore unfamiliar libraries or languages, and reduces repetitive work — allowing you to focus on architecture and problem solving rather than boilerplate code. It supports multiple AI models and integrates with your coding workflow, offering suggestions as you type in real time. """,
          },
    {
        "heading": "💡 ChatGPT & Language Flexibility",
        "importance": "A powerful tool for brainstorming, summarizing, and overcoming language barriers in learning.",
        "content": """ChatGPT — Most People Don’t Know These Simple Things!
 1. You can chat like normal conversation

Just talk casually, the same way you message your friend.
Example: “Hey, tell me in simple way.”

🔹 2. You can switch languages anytime

You can talk in English, Telugu, or mix both.
Example: “Explain this in Telugu.”
Example: “Telugu lo cheppu.”

🔹 3. You don’t need big grammar or technical words

Even small lines are enough:
“Give short notes.”
“Explain in 2 lines.”
“Make it easy.”
🔹 4. You can show images and ask doubts

Just upload a photo and say:
“Explain this diagram.”
“What is this error?”

🔹 5. You can upload PDFs

Ask:
“Summarize this.”
“Give important questions.”
“Explain chapter 1.”

🔹 6. You can learn anything

Coding, maths, English, electronics, interviews—anything in simple steps.

🔹 7. You can ask in your style
 You can say:
“From now, answer in two lines.”
“Talk like my friend.”
“Explain like I’m a beginner.”
You can ask real daily doubts""",
        "link": "https://openai.com/chatgpt"
    },
    {
        "heading": "📺 YouTube Playlist Mastery",
        "importance": "Playlists organize content for structured learning, saving time and ensuring a logical progression through course material.",
        "content": """ YouTube Playlist Option

The YouTube playlist feature allows users to organize videos into collections based on a theme, topic, or learning path. Instead of searching for individual videos every time, you can group related content together, enabling continuous, structured viewing. Playlists can be public, private, or unlisted, giving flexibility in sharing with peers, project teams, or keeping a personal study library. You can create playlists for subjects like Data Structures, Embedded Systems, MATLAB, CAD tutorials, IoT projects, or Python programming, or even for exam preparation content like GATE, aptitude, and placement questions. The playlist automatically plays videos in sequence, which ensures a smooth learning flow without distractions from unrelated content. Importance of YouTube Playlists for Engineering Students

Structured Learning Path:
Engineering subjects often require sequential understanding—for example, in DSA, you must learn arrays → linked lists → trees → graphs. Playlists allow you to organize videos in logical order, ensuring you follow a structured learning path similar to SDLC phases in software projects or stepwise experiments in labs.

Time Efficiency:
Instead of searching for videos repeatedly, a playlist centralizes all relevant content, saving time. This is crucial during final-year projects, internship preparation, or exam preparation when every hour counts.

Revision and Reference:
Playlists serve as a personal library for revisiting concepts. For example, during placement prep, you can have playlists for aptitude tricks, coding challenges, or interview Q&A, enabling quick refresh before tests or interviews.

Collaborative Learning:
You can share playlists with friends or project teammates, ensuring everyone has access to the same curated learning resources, similar to a shared project repository in GitHub or a collaborative Google Drive folder for lab notes.

Enhanced Focus and Reduced Distractions:
Curated playlists remove the need to browse unrelated videos, reducing context switching and keeping attention on technical learning, which improves knowledge retention—critical for complex engineering topics. """, 
    },
    {
        "heading": "🏛️ Civil Services & Govt. Jobs",
        "importance": "Offers high job security, social prestige, and involvement in national project management.",
        "content": """ Civil Services (IAS, IPS, IFS, etc.)

Civil Services are prestigious government positions that involve administration, policymaking, and implementation of programs at the national, state, or local level. For engineering students, civil services offer a career beyond technical roles, allowing you to use analytical, problem-solving, and project management skills in governance. Engineers often have an edge in exam preparation, as subjects like Quantitative Aptitude, Logical Reasoning, and Analytical Writing are part of the preliminary exams (UPSC Prelims). Furthermore, technical knowledge from engineering, like environmental studies, infrastructure planning, IT systems, or renewable energy, can be highly relevant for roles in IAS (Indian Administrative Service), IPS (Indian Police Service), IES (Indian Engineering Services), and specialized posts in defense, railways, and public sector undertakings. Preparing for civil services also improves your general awareness, decision-making skills, and ability to handle large-scale projects, which are transferable to both government and private sector roles. Government Jobs for Engineers

Government jobs for engineers are sector-specific technical roles where your engineering degree is a requirement. Some common opportunities include:

Indian Engineering Services (IES/IES Exam):

Roles in railways, CPWD, defense, public works, power, and telecommunications.

Engineers design, implement, and maintain critical infrastructure systems.

Salary and perks are high, along with structured career growth.

Public Sector Units (PSUs):

Companies like BHEL, ONGC, NTPC, GAIL, ISRO, DRDO, and SAIL recruit engineers via GATE scores or direct recruitment exams.

Work involves core engineering projects, R&D, design, and operations, with excellent pay and stability.

State/Union Government Technical Posts:

Civil, mechanical, electrical, IT, and electronics engineers can apply for state electricity boards, municipal corporations, water resources departments, and transportation sectors.

Defence and Railways:

Engineers can join Indian Navy, Army, Air Force, or Indian Railways in technical capacities, working on weapons systems, electronics, signal engineering, or mechanical maintenance. Engineering Perspective Summary

For engineers, civil services and government jobs provide a parallel career path to the private sector. Your analytical skills, technical knowledge, and problem-solving abilities make you competitive in exams like UPSC, IES, and PSU recruitment. These jobs combine technical expertise with administrative responsibility, offering a blend of high impact, stable career, and opportunities for growth, making them a strategic choice alongside corporate engineering careers.""",
     },
    {
        "heading": "⚙️ Git, GitHub & Non-Tech Roles",
        "importance": "Git/GitHub is the fundamental collaboration tool. Non-tech roles offer specialized high-demand career paths.",
        "content": """ Git – Version Control System for Engineers

Git is a distributed version control system (VCS) used by engineers and developers to track changes in code, documents, or design files over time. Think of it as a time machine for your project: it allows you to save snapshots (commits) of your work, revert to previous versions, and collaborate with team members without overwriting each other’s changes. In engineering projects, whether it’s software development, embedded systems programming, IoT firmware, or simulation scripts, Git ensures code integrity, version history, and efficient collaboration. Engineers use Git to manage branches for different features, experiment with ideas safely, and maintain a clean record of contributions—essential for team-based projects, hackathons, and industrial internships. GitHub – Cloud Repository for Collaboration

GitHub is a cloud-based platform built on Git that allows engineers to host their repositories online, share code, collaborate with peers, and showcase projects publicly or privately. For engineering students, GitHub is more than storage; it acts as a digital portfolio. Recruiters and internship managers can view your repositories to evaluate:

Project complexity and coding standards

Commit history and consistency

Collaboration skills (pull requests, code reviews)

Documentation and README quality

GitHub also supports CI/CD pipelines, issue tracking, and project boards, making it a mini project management platform for software and multidisciplinary engineering projects. For final-year projects, it’s common to host IoT, Python, MATLAB, or CAD simulation code on GitHub, providing professional visibility and version tracking. Non-Technical Roles in Engineering and IT

Not all engineering careers require coding or deep technical work. Many engineers pursue non-technical roles that leverage problem-solving, analytical thinking, project management, or domain knowledge. Examples include:

Project Management:

Coordinating schedules, resources, and deliverables for engineering projects.

Tools like MS Project, Jira, and Trello are used.

Business Analysis:

Translating client requirements into functional specifications.

Engineers with domain knowledge analyze systems, workflows, or processes.

Technical Writing & Documentation:

Creating manuals, reports, API documentation, and research papers.

Important in R&D labs, product design, or software companies.

Quality Assurance (QA) & Testing:

Verifying system functionality, performance, and compliance.

Engineers test hardware circuits, software code, or mechanical systems.

Sales & Marketing for Tech Products:

Engineering graduates often work in technical sales or solution consulting, explaining complex products to clients.

Operations & Supply Chain Management:

Engineers manage manufacturing processes, logistics, or procurement in production-heavy industries.

Non-technical roles are important because they combine engineering understanding with organizational, analytical, and communication skills, allowing engineers to contribute even without coding daily. Engineering Perspective Summary

Git = Local version control, tracks your engineering work step by step.

GitHub = Cloud collaboration platform, showcases your projects and enables team work.

Non-technical roles = Allow engineers to leverage technical thinking in management, analysis, writing, testing, or operations, widening career opportunities beyond software coding.""",
        "link": "https://github.com/",
    },
    {
        "heading": "⭐ Portfolio & IEEE",
        "importance": "These add substantial value to your profile beyond academics, showcasing practical skills and professional networking.",
        "content":"""Portfolio for Engineers

A portfolio is a structured collection of your engineering work that demonstrates skills, projects, certifications, and achievements in one place. Think of it as a digital resume on steroids, showing not just what you know, but what you can do. A strong portfolio helps recruiters, internship managers, or research guides assess your practical abilities quickly.

Example:

Website Portfolio: You create a personal website with sections for:

Projects: IoT-based smart garden, MATLAB simulations, Arduino traffic light controller

Skills: Python, Embedded C, CAD, MATLAB, SQL

Certificates: NPTEL courses, Coursera AI certificate

Achievements: Hackathon participation, IEEE conference paper

This portfolio acts as proof of your engineering skills, making you stand out in internships, placements, and competitions.",IEEE (Institute of Electrical and Electronics Engineers)

IEEE is the world’s largest technical professional organization, focusing on engineering, technology, and innovation. For students, IEEE provides:

Access to research papers, journals, and conferences

Networking opportunities with engineers and researchers worldwide

Student chapters in colleges for workshops, competitions, and technical events

Example:

You join your college IEEE Student Branch.

Attend a workshop on IoT or Robotics, submit a paper on your IoT project, and present it at a conference.

You gain visibility, learn from experts, and add it to your portfolio, boosting your technical credibility. """
    },
    {
        "heading": "🛠️ Lovable.Dev Platform",
        "importance": "If this is a specific resource, it's important for focused learning or community engagement in a defined area.",
        "content": """Lovable Dev: Meaning for Engineers/Developers

A Lovable Developer (Dev) is a software engineer or programmer who is technically competent and easy to work with, making them highly respected and appreciated in a team. Being “lovable” doesn’t mean popularity—it means creating a positive impact through skills, collaboration, and attitude.

A Lovable Dev typically:

Writes clean, readable, and maintainable code that others can easily understand.

Communicates effectively with teammates, clarifying doubts and sharing solutions.

Helps debug issues and mentors juniors without ego.

Adapts to feedback and embraces teamwork, deadlines, and project goals.

Shares knowledge openly, contributing to documentation, GitHub repos, and best practices. Why Being a Lovable Dev Matters

Team Efficiency:

In software projects, a lovable dev reduces confusion, improves collaboration, and ensures smooth code integration.

Professional Growth:

Managers notice developers who are not just skilled but also cooperative and solution-oriented, making them candidates for team lead or senior roles faster.

Reputation in Open Source / Hackathons:

In collaborative environments like GitHub, hackathons, or open-source projects, lovable devs are invited to contribute more, increasing visibility and career opportunities. Small Example

Imagine a team working on a smart garden IoT system:

A lovable dev documents the Arduino code, writes modular Python scripts, helps teammates debug sensor issues, and keeps the GitHub repository organized.

Result: The project is completed efficiently, team morale stays high, and professors or recruiters give higher recognition to the team. """,
        "link": "https://example.com/lovabledev" 
    },
    # 📚 NEW TOPIC: Curriculum Guide
    {
        "heading": "📚 Curriculum Guide & Electives",
        "importance": "Understanding the curriculum helps you prioritize subjects and choose beneficial electives for specialization.",
        "content": """Curriculum in Engineering

The curriculum is a structured plan of study designed to teach engineering students the fundamental concepts, applied skills, and domain-specific knowledge required in their branch. It includes core subjects, labs, projects, electives, seminars, and workshops, providing a roadmap from basic theory to advanced applications. For example, a Computer Science curriculum may start with Programming, Data Structures, and Discrete Mathematics, progress to Operating Systems, Databases, and Networks, and finally include AI, IoT, or Cloud Computing electives in later years.  Importance of Curriculum

Foundation Building:

Core subjects ensure engineers understand fundamental principles like thermodynamics for mechanical, circuits for ECE, or structural analysis for civil engineering.

This foundation allows students to solve real-world engineering problems, design systems, and innovate effectively.

Skill Development:

Labs, projects, and assignments teach practical skills like coding, circuit designing, CAD modeling, or testing.

The curriculum ensures a structured approach, helping students gradually move from simple tasks to complex problem-solving.

Industry Readiness:

By following the curriculum, students become familiar with standard tools, methodologies, and industry practices, such as SDLC, Agile, simulation software, or civil design codes.

This prepares students for internships, placements, and higher studies. Curriculum Guide

A curriculum guide is a document or roadmap that helps students understand subject sequencing, credit requirements, and specialization opportunities. It tells students:

Which courses are mandatory (core) and which are optional (electives)

Prerequisites for advanced subjects

Recommended projects, workshops, and labs for skill development

Alignment with industry standards, accreditation, and employability goals

For example, a guide may suggest:

Year 1–2: Fundamentals and basic labs

Year 3: Core specialization subjects + mini projects

Year 4: Electives + major projects + internships  Electives in Engineering

Electives are optional courses that allow students to specialize in areas of interest within or outside their branch. They provide flexibility to explore emerging technologies or cross-disciplinary skills.

Examples:

Computer Science: AI, Machine Learning, Cloud Computing, Cybersecurity

Mechanical: Renewable Energy, Automotive Design, Robotics

Civil: Smart Cities, Earthquake Engineering, Advanced Construction Materials

ECE: VLSI Design, IoT, Wireless Communication

Electives help students:

Gain domain-specific expertise

Align studies with career goals

Stand out in placements, internships, or higher studies """,
        }
]


# --- 2. Flask Routes ---

@app.route('/')
def index():
    """Renders the main HTML page with the career data."""
    # The career_data list is passed to the HTML template
    return render_template('index.html', career_data=CONTENT_DATA)

@app.route('/chat', methods=['POST'])
def chat():
    """Handles the AI chat requests using the Gemini API."""
    data = request.json
    user_message = data.get("message")

    if not user_message:
        return jsonify({"response": "Please provide a message."})

    # The AI is specifically tuned to be an Engineering Career Assistant
    prompt = (
        f"You are an Engineering Career Assistant. Your goal is to provide concise, encouraging, "
        f"and accurate advice. The user is asking for help with their career. "
        f"Base your answer on the engineering career topics: {', '.join([d['heading'] for d in CONTENT_DATA])}. "
        f"If the question is technical, keep the explanation simple but precise. "
        f"User query: '{user_message}'"
    )

    try:
        # Call the Gemini API with the specialized prompt
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[prompt]
        )
        ai_response = response.text
        return jsonify({"response": ai_response})
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        # Return a user-friendly error message
        return jsonify({"response": "Sorry, I am currently unable to connect to the AI service. Please try again later."}), 500

if __name__ == '__main__':
    # Ensure you have a 'templates' folder with 'index.html' inside.
    app.run(debug=True, port=5000)