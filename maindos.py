import os
import glob

# Define the results directory
results_dir = "results"

# Find all plots in the results directory
plot_files = glob.glob(os.path.join(results_dir, "*.pdf"))

# Define the Markdown file
markdown_file = os.path.join(results_dir, "vulnerability_proneness_report.md")

# Start writing the Markdown content
markdown_content = """
# Vulnerability Proneness Analysis Report

## (RQ1) Vulnerability Prevalence of Third-Party Actions

We used a mixed-methods approach—quantitative and qualitative analyses—to investigate vulnerability-proneness across GitHub Marketplace categories.

### Methodology

To address RQ1, we examined how vulnerability-proneness varies across GitHub Marketplace categories, considering both direct vulnerabilities from the source code and indirect risks from dependencies.

We first assessed whether certain categories exhibit distinct vulnerability-proneness using the **Shapiro-Wilk test** to check for normality. Since deviations were detected, we applied the **Kruskal-Wallis test**, a non-parametric method suited for comparing multiple groups.

#### Hypothesis
- **H₀₁:** Vulnerability-proneness does not significantly differ across categories.

Rejecting **H₀₁** would indicate that vulnerability risks are not evenly distributed across categories, suggesting the need for further investigation into category-specific security challenges.

Beyond category-level differences, we examined the role of dependencies, comparing source code vulnerabilities against total vulnerability-proneness, which includes both direct and dependency-related risks.

- **H₀₂:** No significant differences exist between vulnerabilities found in the source code and those observed in overall vulnerability-proneness across categories.

To refine our analysis, we conducted **Mann-Whitney pairwise comparisons** with **Holm’s correction**, considering results significant at *p < 0.05*. We further evaluated **Cliff’s delta effect sizes** to assess practical significance.

### Results

#### Statistical Analysis
The Kruskal-Wallis test yielded the following results:

- **Test Statistic:** 12.2267
- **p-value:** 0.4276

A p-value greater than 0.05 suggests no statistically significant differences among categories in terms of vulnerability-proneness.

### Visualizations
Below are the key visualizations generated in our analysis:
"""

# Embed generated plots
for plot_file in plot_files:
    plot_name = os.path.basename(plot_file)
    markdown_content += f"\n![]({plot_name})\n"

# Conclude the report
markdown_content += """

### Key Takeaways
- No significant differences in vulnerability-proneness were detected across categories.
- Further investigation is needed to assess structural differences in security risks.
- A qualitative analysis of CWE distributions provides additional insight into security concerns within GitHub Actions.

This report serves as a foundation for further research into vulnerability prevalence and mitigation strategies.
"""

# Write the Markdown file
with open(markdown_file, "w") as md_file:
    md_file.write(markdown_content)

print(f"Markdown report generated: {markdown_file}")
