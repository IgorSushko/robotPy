---
name: HTML-CSS-Flexbox
description: Prefer Flexbox for layout when generating or modifying HTML/CSS, while preserving existing functionality
---

# Skill Instructions

## 1. Analyze First
- Review provided HTML, CSS, and JS files
- Identify current layout techniques (float, inline-block, table, grid, etc.)
- Determine if Flexbox is appropriate for the specific layout

## 2. Apply Flexbox When Beneficial
- Use Flexbox for:
  - Horizontal or vertical alignment
  - Centering elements
  - Distributing space between elements
  - Responsive layouts

- Replace outdated layout methods when safe:
  - float
  - inline-block (for layout purposes)
  - table-based layouts (if not semantic)

## 3. Preserve Existing Behavior
- DO NOT break:
  - JavaScript functionality
  - element IDs and class names (unless necessary)
  - event bindings
- Keep structure changes minimal and targeted

## 4. When Generating New Code
- Use Flexbox as the default layout system
- Follow best practices:
  - use `display: flex`
  - prefer `gap` over margins for spacing
  - use `justify-content` and `align-items` properly
  - avoid unnecessary nesting

## 5. Avoid Over-Engineering
- Do NOT rewrite entire layouts if not required
- Do NOT replace CSS Grid if it is already correctly used
- Do NOT introduce Flexbox where it provides no benefit

## 6. Output Requirements
- Provide complete updated files when modifying code
- Keep formatting clean and readable
- Ensure the result is responsive where possible