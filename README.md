# Enhancing the Security of a GitHub Project

## Overview

For this activity, I enhanced the security of a GitHub repository by enabling multiple GitHub security features and repository protection mechanisms.

The aim of this task was to improve the repository’s overall security posture using GitHub’s built-in security tools and preventative security controls.

---

## Security Enhancements Implemented

The following security improvements were implemented within the repository:

- Dependabot alerts
- Dependabot security updates
- CodeQL code scanning
- Secret protection
- Push protection
- Branch protection rules
- SECURITY.md vulnerability disclosure policy

---

## Explanation of Security Features

### Dependabot Alerts

Dependabot alerts help identify vulnerable or outdated dependencies used within the repository. This assists developers in discovering security vulnerabilities in third-party packages before they can be exploited.

### Dependabot Security Updates

Dependabot security updates automatically recommend or create updates for vulnerable dependencies. This reduces the risk of using outdated or insecure software components.

### CodeQL Code Scanning

CodeQL performs static code analysis on repository code to identify insecure coding practices, vulnerabilities, and potential security weaknesses.

### Secret Protection

Secret protection helps detect accidentally exposed credentials, API keys, authentication tokens, or other sensitive information inside repository files.

### Push Protection

Push protection prevents sensitive secrets from being accidentally pushed into the repository by blocking commits containing detected secrets.

### Branch Protection Rules

Branch protection rules improve repository integrity by preventing unsafe or unauthorised direct modifications to the main branch.

The following protections were implemented:
- require pull requests before merging
- block force pushes

### SECURITY.md Policy

A SECURITY.md file was added to establish a responsible vulnerability disclosure process for reporting security issues.

---

## Why This Is a Strong Security Implementation

These security controls improve the repository’s security posture by implementing automated vulnerability monitoring, dependency management, code analysis, secret detection, and safer collaboration practices.

This implementation helps reduce risks related to:
- insecure dependencies
- exposed credentials
- insecure code
- unauthorised repository modifications
- accidental secret leakage

The use of preventative and automated security controls reflects modern software security and DevSecOps best practices.

---

## Evidence

Screenshots included:
1. Repository homepage
2. Dependabot configuration
3. CodeQL code scanning enabled
4. Secret protection enabled
5. Push protection enabled
6. Branch protection rule configuration
7. SECURITY.md file

---

## Reflection

This activity demonstrated how GitHub’s built-in security features can significantly improve repository security using practical and automated security mechanisms.

It also demonstrated the importance of proactive security practices such as vulnerability management, secure collaboration controls, code analysis, and protection against accidental exposure of sensitive information.
