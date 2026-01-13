/**
 * PAPER-CODE Templates Package
 *
 * This package provides reusable Jinja2 templates for documentation generation.
 * Use with PAPER-CODE CLI or integrate directly into your tooling.
 *
 * @example
 * // With PAPER-CODE CLI
 * paper-code init --template-dir ./node_modules/@paper-code/templates
 *
 * @example
 * // In Node.js
 * const path = require('path');
 * const templatesDir = path.join(__dirname, 'core');
 */

const path = require("path");

module.exports = {
  // Get path to templates directory
  getTemplatesPath: () => __dirname,

  // Get specific template directory
  getCoreTemplates: () => path.join(__dirname, "core"),
  getAITemplates: () => path.join(__dirname, "ai"),
  getStacksTemplates: () => path.join(__dirname, "stacks"),
  getLibsTemplates: () => path.join(__dirname, "libs"),
  getGitHubTemplates: () => path.join(__dirname, "github"),

  // Get all available templates info
  getTemplatesInfo: () => ({
    version: require("./package.json").version,
    path: __dirname,
    templates: {
      core: path.join(__dirname, "core"),
      ai: path.join(__dirname, "ai"),
      stacks: path.join(__dirname, "stacks"),
      libs: path.join(__dirname, "libs"),
      github: path.join(__dirname, "github"),
    },
    description: "Official PAPER-CODE documentation templates",
  }),
};
