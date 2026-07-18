/**
 * Friday Frontend — Utility Functions
 *
 * Shared utilities used across the application.
 * This is also where shadcn/ui's `cn()` helper lives.
 */

import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

/**
 * Merges Tailwind CSS classes intelligently.
 * Combines clsx for conditional classes with tailwind-merge
 * to resolve conflicting utility classes.
 */
export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
