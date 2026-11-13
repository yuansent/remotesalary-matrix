import json

# Top 12 tech roles
roles = [
    {"slug": "senior-frontend-engineer", "title": "Senior Frontend Engineer", "us_base": 155000, "skills": ["React", "TypeScript", "Next.js", "Performance"]},
    {"slug": "senior-backend-engineer", "title": "Senior Backend Engineer", "us_base": 165000, "skills": ["Go", "Python", "Distributed Systems", "PostgreSQL"]},
    {"slug": "full-stack-developer", "title": "Full Stack Developer", "us_base": 140000, "skills": ["Node.js", "React", "Cloud Infrastructure", "API Design"]},
    {"slug": "devops-cloud-architect", "title": "DevOps & Cloud Architect", "us_base": 170000, "skills": ["Kubernetes", "AWS", "Terraform", "CI/CD"]},
    {"slug": "ai-machine-learning-engineer", "title": "AI / Machine Learning Engineer", "us_base": 185000, "skills": ["PyTorch", "LLM Fine-tuning", "Vector DBs", "Python"]},
    {"slug": "mobile-engineer-ios-android", "title": "Mobile Engineer (iOS/Android)", "us_base": 150000, "skills": ["React Native", "Flutter", "Swift", "Kotlin"]},
    {"slug": "senior-product-designer", "title": "Senior Product Designer (UI/UX)", "us_base": 135000, "skills": ["Figma", "Design Systems", "User Research", "Prototyping"]},
    {"slug": "engineering-manager", "title": "Engineering Manager", "us_base": 195000, "skills": ["Team Leadership", "Agile", "Hiring", "Tech Strategy"]},
    {"slug": "data-engineer", "title": "Data Engineer", "us_base": 150000, "skills": ["Snowflake", "dbt", "Airflow", "SQL / Python"]},
    {"slug": "qa-automation-lead", "title": "QA Automation Lead", "us_base": 125000, "skills": ["Playwright", "Cypress", "End-to-End Testing", "CI Automation"]},
    {"slug": "security-engineer", "title": "Application Security Engineer", "us_base": 165000, "skills": ["AppSec", "Penetration Testing", "SOC 2", "Cloud Security"]},
    {"slug": "technical-product-manager", "title": "Technical Product Manager", "us_base": 150000, "skills": ["Product Discovery", "PRD Writing", "Data Analysis", "Roadmapping"]}
]

# Top 25 global talent countries with accurate cost-of-labor ratio, tax, and compliance models
countries = [
    {
        "code": "PL", "country": "Poland", "currency": "PLN", "rate_to_usd": 0.25,
        "ratio": 0.48, "tax_pct": 19, "eor_risk": "Low (B2B flat tax common)",
        "contract_mode": "B2B Flat Tax (Ryczałt 12%) or EOR (Deel/Remote)",
        "ip_protection": "EU Directive Strong IP assignment",
        "best_eor": "Deel / Remote.com ($599/mo)"
    },
    {
        "code": "RO", "country": "Romania", "currency": "RON", "rate_to_usd": 0.22,
        "ratio": 0.42, "tax_pct": 16, "eor_risk": "Low (SRL micro-company)",
        "contract_mode": "Micro-Enterprise B2B or EOR",
        "ip_protection": "EU High Standard",
        "best_eor": "Deel ($599/mo)"
    },
    {
        "code": "UA", "country": "Ukraine", "currency": "UAH", "rate_to_usd": 0.024,
        "ratio": 0.38, "tax_pct": 5, "eor_risk": "Medium (Diia City contractor model)",
        "contract_mode": "Diia City Gig-Contract or Private Entrepreneur (FOP 5%)",
        "ip_protection": "Specific IP transfer deeds mandatory",
        "best_eor": "Deel ($599/mo)"
    },
    {
        "code": "PT", "country": "Portugal", "currency": "EUR", "rate_to_usd": 1.08,
        "ratio": 0.45, "tax_pct": 25, "eor_risk": "Medium (Worker misclassification scrutiny)",
        "contract_mode": "Recibos Verdes (Sole Trader) or EOR",
        "ip_protection": "EU Standard",
        "best_eor": "Remote.com / Deel"
    },
    {
        "code": "ES", "country": "Spain", "currency": "EUR", "rate_to_usd": 1.08,
        "ratio": 0.50, "tax_pct": 28, "eor_risk": "High (Strict autonomo falso labor laws)",
        "contract_mode": "Autónomo or Mandatory EOR for exclusive full-time",
        "ip_protection": "EU Strict IP Protection",
        "best_eor": "Remote.com ($599/mo)"
    },
    {
        "code": "DE", "country": "Germany", "currency": "EUR", "rate_to_usd": 1.08,
        "ratio": 0.75, "tax_pct": 38, "eor_risk": "Very High (Scheinselbständigkeit / Fake Freelance)",
        "contract_mode": "Strict EOR or Local GmbH Subsidary",
        "ip_protection": "Strict Moral Rights retention (UrhG)",
        "best_eor": "WorkMotion / Remote.com"
    },
    {
        "code": "GB", "country": "United Kingdom", "currency": "GBP", "rate_to_usd": 1.28,
        "ratio": 0.78, "tax_pct": 32, "eor_risk": "High (IR35 off-payroll rules)",
        "contract_mode": "Outside IR35 Contractor or EOR / Direct PAYE",
        "ip_protection": "UK Copyright & Patents Act",
        "best_eor": "Remote.com / Deel"
    },
    {
        "code": "IN", "country": "India", "currency": "INR", "rate_to_usd": 0.012,
        "ratio": 0.28, "tax_pct": 20, "eor_risk": "Low (Private Limited / Sole Prop B2B)",
        "contract_mode": "Independent Consultancy Agreement or EOR",
        "ip_protection": "Indian Copyright Act requires express written assignment",
        "best_eor": "Deel / Multiplier ($300/mo)"
    },
    {
        "code": "BR", "country": "Brazil", "currency": "BRL", "rate_to_usd": 0.17,
        "ratio": 0.38, "tax_pct": 15, "eor_risk": "High (CLT vs PJ labor courts favor workers)",
        "contract_mode": "PJ (Pessoa Jurídica B2B) or CLT via EOR",
        "ip_protection": "Explicit IP assignment clause in English + Portuguese",
        "best_eor": "Deel ($599/mo) / Remote"
    },
    {
        "code": "AR", "country": "Argentina", "currency": "ARS", "rate_to_usd": 0.001,
        "ratio": 0.32, "tax_pct": 12, "eor_risk": "Low (USD cross-border wire preferred)",
        "contract_mode": "Monotributo / USD Contractor Agreement",
        "ip_protection": "Civil Code IP Assignment",
        "best_eor": "Ontop / Deel"
    },
    {
        "code": "CO", "country": "Colombia", "currency": "COP", "rate_to_usd": 0.00025,
        "ratio": 0.30, "tax_pct": 18, "eor_risk": "Medium (Prestación de Servicios contract)",
        "contract_mode": "Prestación de Servicios or EOR",
        "ip_protection": "Decisión Andina 351 IP Compliance",
        "best_eor": "Deel / Ontop"
    },
    {
        "code": "MX", "country": "Mexico", "currency": "MXN", "rate_to_usd": 0.051,
        "ratio": 0.40, "tax_pct": 20, "eor_risk": "High (2021 Subcontracting Reform ban)",
        "contract_mode": "RESICO Independent Contractor or REPSE EOR",
        "ip_protection": "Federal Copyright Law requires recorded transfer",
        "best_eor": "Deel / Remote.com"
    },
    {
        "code": "PH", "country": "Philippines", "currency": "PHP", "rate_to_usd": 0.017,
        "ratio": 0.24, "tax_pct": 15, "eor_risk": "Low (BPO independent contractor)",
        "contract_mode": "Independent Contractor or EOR (13th Month Pay mandatory)",
        "ip_protection": "Intellectual Property Code of Philippines",
        "best_eor": "Deel / Multiplier ($300/mo)"
    },
    {
        "code": "VN", "country": "Vietnam", "currency": "VND", "rate_to_usd": 0.000039,
        "ratio": 0.25, "tax_pct": 10, "eor_risk": "Medium (Individual business household)",
        "contract_mode": "Service Contract or EOR",
        "ip_protection": "Intellectual Property Law 2005",
        "best_eor": "Multiplier / Deel"
    },
    {
        "code": "NG", "country": "Nigeria", "currency": "NGN", "rate_to_usd": 0.00065,
        "ratio": 0.20, "tax_pct": 12, "eor_risk": "Low (Direct FX Contractor)",
        "contract_mode": "B2B Contractor Agreement paid in USD/USDC",
        "ip_protection": "Copyright Act 2022",
        "best_eor": "Deel / Raenest"
    },
    {
        "code": "KE", "country": "Kenya", "currency": "KES", "rate_to_usd": 0.0077,
        "ratio": 0.22, "tax_pct": 15, "eor_risk": "Low (Silicon Savannah talent)",
        "contract_mode": "Independent Consultant Agreement",
        "ip_protection": "Industrial Property Act",
        "best_eor": "Deel / Remote"
    },
    {
        "code": "ZA", "country": "South Africa", "currency": "ZAR", "rate_to_usd": 0.055,
        "ratio": 0.35, "tax_pct": 26, "eor_risk": "Medium (Section 200A labor presumption)",
        "contract_mode": "Independent Contractor or EOR",
        "ip_protection": "Copyright Act 1978",
        "best_eor": "Deel / Remote"
    },
    {
        "code": "EG", "country": "Egypt", "currency": "EGP", "rate_to_usd": 0.02,
        "ratio": 0.22, "tax_pct": 14, "eor_risk": "Low (Freelancer tech boom)",
        "contract_mode": "USD Offshore Contractor",
        "ip_protection": "Law No. 82 of 2002",
        "best_eor": "Deel / Multiplier"
    },
    {
        "code": "PK", "country": "Pakistan", "currency": "PKR", "rate_to_usd": 0.0036,
        "ratio": 0.18, "tax_pct": 5, "eor_risk": "Low (PSEB 0.25% export tech tax exemption)",
        "contract_mode": "IT Export Contractor Agreement",
        "ip_protection": "Copyright Ordinance 1962",
        "best_eor": "Deel / Multiplier"
    },
    {
        "code": "TR", "country": "Turkey", "currency": "TRY", "rate_to_usd": 0.028,
        "ratio": 0.30, "tax_pct": 20, "eor_risk": "Medium (Technopark / Sole Prop)",
        "contract_mode": "Sole Trader B2B or EOR",
        "ip_protection": "IP Law No. 6769",
        "best_eor": "Deel"
    },
    {
        "code": "CA", "country": "Canada", "currency": "CAD", "rate_to_usd": 0.72,
        "ratio": 0.82, "tax_pct": 33, "eor_risk": "Medium (CRA employee vs contractor tests)",
        "contract_mode": "Incorporated Contractor (Personal Services Corp) or EOR",
        "ip_protection": "Patent Act / Copyright Act",
        "best_eor": "Remote.com / Deel"
    },
    {
        "code": "AU", "country": "Australia", "currency": "AUD", "rate_to_usd": 0.65,
        "ratio": 0.80, "tax_pct": 32, "eor_risk": "High (Superannuation guarantee on contractors)",
        "contract_mode": "ABN Contractor (Subject to Super) or EOR",
        "ip_protection": "Copyright Act 1968",
        "best_eor": "Remote.com / Deel"
    },
    {
        "code": "CZ", "country": "Czech Republic", "currency": "CZK", "rate_to_usd": 0.043,
        "ratio": 0.46, "tax_pct": 15, "eor_risk": "Medium (Švarcsystém illegal contractor laws)",
        "contract_mode": "Trade License (Živnostenský list) or EOR",
        "ip_protection": "EU Civil Code IP assignment",
        "best_eor": "Remote.com / Deel"
    },
    {
        "code": "EE", "country": "Estonia", "currency": "EUR", "rate_to_usd": 1.08,
        "ratio": 0.52, "tax_pct": 20, "eor_risk": "Low (e-Residency OÜ company model)",
        "contract_mode": "Estonian OÜ (0% corporate tax on reinvested profit)",
        "ip_protection": "EU Leading Digital IP Standard",
        "best_eor": "Xolo / Deel"
    },
    {
        "code": "TW", "country": "Taiwan", "currency": "TWD", "rate_to_usd": 0.031,
        "ratio": 0.42, "tax_pct": 18, "eor_risk": "Low (Hardware/Software dual talent)",
        "contract_mode": "Independent Service Contractor or EOR",
        "ip_protection": "Copyright Act of Taiwan",
        "best_eor": "Multiplier / Deel"
    }
]

# Generate Matrix of 12 x 25 = 300 rich benchmark profiles
matrix = []
for r in roles:
    for c in countries:
        local_annual_usd = int(r["us_base"] * c["ratio"])
        monthly_usd = int(local_annual_usd / 12)
        hourly_usd = round(local_annual_usd / 2080, 2)
        savings_annual = r["us_base"] - local_annual_usd
        savings_pct = round((savings_annual / r["us_base"]) * 100)
        
        matrix.append({
            "role_slug": r["slug"],
            "role_title": r["title"],
            "country_code": c["code"],
            "country_name": c["country"],
            "us_base_annual": r["us_base"],
            "local_annual_usd": local_annual_usd,
            "monthly_usd": monthly_usd,
            "hourly_usd": hourly_usd,
            "annual_savings_usd": savings_annual,
            "savings_pct": savings_pct,
            "tax_pct": c["tax_pct"],
            "eor_risk": c["eor_risk"],
            "contract_mode": c["contract_mode"],
            "ip_protection": c["ip_protection"],
            "best_eor": c["best_eor"],
            "skills": r["skills"]
        })

with open("./data/matrix.json", "w") as f:
    json.dump(matrix, f, indent=2)

with open("./data/roles.json", "w") as f:
    json.dump(roles, f, indent=2)

with open("./data/countries.json", "w") as f:
    json.dump(countries, f, indent=2)

print(f"Generated {len(matrix)} role x country salary benchmarks successfully!")
