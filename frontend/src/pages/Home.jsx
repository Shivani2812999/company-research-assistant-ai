import { useState } from "react";
import api from "../services/api";
import {
    FaSearch,
    FaRobot,
    FaBuilding,
    FaBoxOpen,
    FaExclamationTriangle,
    FaGlobe,
    FaDownload,
    FaBolt,
} from "react-icons/fa";

function Home() {
    const [query, setQuery] = useState("");
    const [model, setModel] = useState("openai/gpt-4o-mini");
    const [loading, setLoading] = useState(false);
    const [result, setResult] = useState(null);

    const handleDownloadPDF = async () => {
    if (!result?.pdf) {
        alert("No report available to download yet.");
        return;
    }

    const filename = result.pdf.split("/").pop().split("\\").pop();
    console.log("Downloading:", filename);

    try {
        const response = await api.get(
            `/reports/${encodeURIComponent(filename)}`,
            { responseType: "blob" }
        );

        const url = window.URL.createObjectURL(
            new Blob([response.data], { type: "application/pdf" })
        );
        const link = document.createElement("a");
        link.href = url;
        link.download = filename;
        document.body.appendChild(link);
        link.click();
        link.remove();
        window.URL.revokeObjectURL(url);
    } catch (error) {
        const errText = await error.response?.data?.text?.().catch(() => null);
        console.error("Download failed:", error.response?.status, errText);
        alert("Failed to download PDF");
    }
};






    const handleResearch = async () => {
        if (!query.trim()) {
            alert("Please enter a company name or website");
            return;
        }

        setLoading(true);
        setResult(null);

        try {
            const response = await api.post("/research", {
                query,
                model,
            });

            setResult(response.data);
        } catch (error) {
            console.error(error);
            alert("Something went wrong while generating the report.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="home-page">
            {/* Hero Section */}
            <section className="hero">
                <h1>
                    <FaRobot />
                    AI Company Research Assistant
                </h1>

                <p>
                    Discover companies, analyze products, identify competitors, and
                    generate detailed AI-powered business reports in seconds.
                </p>
            </section>

            {/* Search Card */}
            <div className="search-card">
                <div className="input-group">
                    <FaSearch className="input-icon" />

                    <input
                        type="text"
                        placeholder="Enter company name or website..."
                        value={query}
                        onChange={(e) => setQuery(e.target.value)}
                        onKeyDown={(e) => {
                            if (e.key === "Enter") {
                                handleResearch();
                            }
                        }}
                    />
                </div>

                <div className="controls">
                    <select
                        value={model}
                        onChange={(e) => setModel(e.target.value)}
                    >
                        <option value="openai/gpt-4o-mini">
                            GPT-4o Mini
                        </option>

                        <option value="meta-llama/llama-3.3-70b-instruct">
                            Llama 3.3 70B
                        </option>

                        <option value="google/gemini-2.5-flash">
                            Gemini Flash
                        </option>
                    </select>

                    <button
                        className="generate-btn"
                        onClick={handleResearch}
                        disabled={loading}
                    >
                        <FaBolt />

                        {loading ? "Researching..." : "Generate Report"}
                    </button>
                </div>
            </div>

            {/* Loader */}

            {loading && (
                <div className="loader-card">
                    <div className="spinner"></div>

                    <h2>Researching Company...</h2>

                    <p>🔍 Finding company website...</p>
                    <p>🌐 Scraping website...</p>
                    <p>🧠 Running AI analysis...</p>
                    <p>📄 Generating report...</p>
                </div>
            )}

            {/* Result */}

            {result && !loading && (
                <div className="report-container">

                    {/* Summary */}

                    <div className="report-card">
                        <h2>
                            <FaBuilding />
                            Company Summary
                        </h2>

                        <p>
                            {result.analysis?.company_summary}
                        </p>
                    </div>

                    {/* Products */}

                    <div className="report-card">
                        <h2>
                            <FaBoxOpen />
                            Products & Services
                        </h2>

                        <p>
                            {result.analysis?.products_services}
                        </p>
                    </div>

                    {/* Pain Points + Competitors */}

                    <div className="grid">

                        <div className="report-card">
                            <h2>
                                <FaExclamationTriangle />
                                Pain Points
                            </h2>

                            <div className="badge-container">
                                {result.analysis?.pain_points?.map((item, index) => (
                                    <span
                                        key={index}
                                        className="badge danger"
                                    >
                                        {item}
                                    </span>
                                ))}
                            </div>
                        </div>

                        <div className="report-card">
                            <h2>
                                <FaBuilding />
                                Competitors
                            </h2>

                            <div className="badge-container">
                                {result.analysis?.competitors?.map((item, index) => (
                                    <span
                                        key={index}
                                        className="badge primary"
                                    >
                                        {item}
                                    </span>
                                ))}
                            </div>
                        </div>

                    </div>

                    {/* Website */}

                    <div className="report-card">
                        <h2>
                            <FaGlobe />
                            Company Website
                        </h2>

                        <a
                            href={result.website}
                            target="_blank"
                            rel="noopener noreferrer"
                        >
                            {result.website}
                        </a>
                    </div>

                    {/* Download */}

                    <div className="download-section">
                        <button className="download-btn" onClick={handleDownloadPDF}>
                            <FaDownload />
                            Download PDF
                        </button>
                    </div>

                </div>
            )}
        </div>
    );
}

export default Home;


