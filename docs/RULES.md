# RULES.md

**Project:** AI Life Operating System (Codename: FRIDAY)\
**Version:** 1.0

------------------------------------------------------------------------

# Purpose

This document defines the engineering, architectural, and AI coding
standards for the project. Every implementation must follow these rules
unless an approved architectural decision changes them.

------------------------------------------------------------------------

# Core Engineering Principles

-   Write maintainable code over clever code.
-   Prefer readability over micro-optimizations.
-   Build reusable modules.
-   Keep business logic independent from the UI.
-   Every feature must be testable.
-   Documentation is part of the implementation.

------------------------------------------------------------------------

# Technology Rules

## Frontend

-   Next.js App Router
-   React
-   TypeScript only
-   Tailwind CSS
-   shadcn/ui
-   Functional components only

Never use: - JavaScript - Inline styles - jQuery

## Backend

-   FastAPI
-   Python 3.12+
-   SQLAlchemy 2.x
-   Alembic
-   Async endpoints

------------------------------------------------------------------------

# Architecture Rules

-   Follow Clean Architecture.
-   Separate UI, business logic and data access.
-   Never place database logic inside UI components.
-   Services communicate through clear interfaces.
-   Avoid circular dependencies.

------------------------------------------------------------------------

# Code Style

-   Strict typing everywhere.
-   No `any` unless unavoidable.
-   Meaningful variable names.
-   Small focused functions.
-   Maximum function length: \~50 lines where practical.
-   Prefer composition over inheritance.

------------------------------------------------------------------------

# Folder Rules

Each feature should contain:

-   Components
-   Hooks
-   Services
-   Types
-   Tests
-   Documentation (when needed)

------------------------------------------------------------------------

# Git Rules

Branch naming:

-   feature/\*
-   fix/\*
-   refactor/\*
-   docs/\*
-   chore/\*

Commit format:

-   feat:
-   fix:
-   refactor:
-   docs:
-   test:
-   chore:

------------------------------------------------------------------------

# API Rules

-   RESTful endpoints
-   Versioned APIs (`/api/v1`)
-   Consistent error responses
-   Input validation
-   Proper HTTP status codes

------------------------------------------------------------------------

# Database Rules

-   UUID primary keys
-   Foreign keys for relationships
-   Soft delete where appropriate
-   Indexed frequently queried fields
-   Never expose internal IDs unnecessarily

------------------------------------------------------------------------

# Security Rules

-   HTTPS only
-   Hash passwords
-   JWT authentication
-   Validate all user input
-   Sanitize file uploads
-   Never expose secrets in code
-   Use environment variables

------------------------------------------------------------------------

# AI Development Rules

The AI should:

-   Preserve user privacy
-   Never fabricate stored memories
-   Ask for clarification when context is insufficient
-   Explain failures clearly
-   Use long-term context when available

The AI should never:

-   Invent facts about the user
-   Delete user data automatically
-   Modify critical settings without confirmation

------------------------------------------------------------------------

# UI Rules

-   Mobile-first
-   Responsive
-   Accessible
-   Keyboard navigable
-   Dark mode supported
-   Consistent spacing
-   Consistent typography

------------------------------------------------------------------------

# Performance Rules

-   Lazy load heavy components
-   Cache expensive operations
-   Optimize database queries
-   Avoid unnecessary re-renders
-   Paginate large datasets

------------------------------------------------------------------------

# Testing Rules

-   Unit tests for business logic
-   Integration tests for APIs
-   End-to-end tests for critical flows

Critical features must not ship without tests.

------------------------------------------------------------------------

# Documentation Rules

Every major feature should include:

-   Purpose
-   Architecture
-   API changes
-   Database changes
-   Known limitations

------------------------------------------------------------------------

# Error Handling

-   Never fail silently.
-   Display user-friendly messages.
-   Log technical details separately.
-   Recover gracefully whenever possible.

------------------------------------------------------------------------

# Definition of Done

A task is complete only when:

-   Feature works as intended
-   Code reviewed
-   Tests pass
-   Documentation updated
-   No critical bugs remain
-   Performance acceptable
-   Accessibility maintained

------------------------------------------------------------------------

# Golden Rule

Every decision should answer:

> "Will this make the product easier to maintain, easier to scale, and
> better for the user?"

If not, reconsider the implementation.
