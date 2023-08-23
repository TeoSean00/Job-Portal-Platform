/**
 * Referred to this for the setup:
 * https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/linting/README.md
 */
module.exports = {
  root: true,
  /**
   * Rely on ignorePatterns rather than .eslintignore as there can only be one of it active in
   * the same working directory.
   */
  ignorePatterns: [
    "node_modules",
    ".webpack",
    ".vscode",
    "*.js",
    "*.spec.ts",
    "cypress",
  ],
  parser: "@typescript-eslint/parser",
  // env: {
  //   jest: true, // For testing purposes
  // },
  parserOptions: {
    tsconfigRootDir: __dirname,
    project: ["tsconfig.json"],
  },
  plugins: [
    "@typescript-eslint",
    "@next/next",
    "react",
    //"jest", // For testing purposes
    //"jest-dom", // For testing purposes
    //"testing-library", // For testing purposes
    "prettier",
  ],
  extends: [
    // https://stackoverflow.com/questions/68878189/eslint-definition-for-rule-import-extensions-was-not-found
    "airbnb-base",

    // https://github.com/iamturns/eslint-config-airbnb-typescript
    "airbnb-typescript/base",
    "plugin:@typescript-eslint/recommended",

    // https://github.com/typescript-eslint/typescript-eslint/blob/master/docs/getting-started/linting/TYPED_LINTING.md
    "plugin:@typescript-eslint/recommended-requiring-type-checking",
    //"plugin:jest/recommended", // For testing purposes
    //"plugin:jest-dom/recommended", // For testing purposes
    //"plugin:testing-library/react",

    // https://nextjs.org/docs/basic-features/eslint
    "plugin:@next/next/recommended",
    "plugin:react-hooks/recommended",
    /**
     * https://github.com/prettier/eslint-plugin-prettier#recommended-configuration
     * "This plugin ships with a plugin:prettier/recommended config that sets up both the
     * plugin and eslint-config-prettier in one go."
     * - advisable to be last extension
     */
    "plugin:prettier/recommended",

    // ! Default Next.js eslint config
    "next/core-web-vitals",
  ],
  rules: {
    // Disabled to allow expect.any() to work
    "@typescript-eslint/no-unsafe-assignment": "off",
    // Let TypeScript handle unused variables
    "@typescript-eslint/no-unused-vars": "off",

    // Force the use of import type if import is only used for type purposes
    "@typescript-eslint/consistent-type-imports": [
      "error",
      { prefer: "type-imports" },
    ],
    "import/extensions": 0,
    // Ensure imports are ordered to keep things tidy
    "import/order": [
      "error",
      {
        groups: ["type", "builtin", "external", "parent", "sibling", "index"],
        "newlines-between": "always",
        alphabetize: { order: "asc" },
      },
    ],
    // Standardise the use of named exports regardless if number of exports is 1
    "import/prefer-default-export": "off",
    "react-hooks/exhaustive-deps": "off",
    // Ensure imports are always relative
    "no-restricted-imports": ["error", { patterns: ["src/*"] }],
    // Let TypeScript handle unused variables
    "no-unused-vars": "off",

    // https://stackoverflow.com/questions/44939304/eslint-should-be-listed-in-the-projects-dependencies-not-devdependencies
    "import/no-extraneous-dependencies": ["error", { devDependencies: true }],

    // https://github.com/yannickcr/eslint-plugin-react/blob/master/docs/rules/jsx-sort-props.md
    "react/jsx-sort-props": [
      "error",
      {
        callbacksLast: true,
        shorthandFirst: true,
        ignoreCase: true,
        reservedFirst: true,
      },
    ],

    // Allow async functions to be used on form submit
    "@typescript-eslint/no-misused-promises": [
      "error",
      { checksVoidReturn: false },
    ],
    "arrow-body-style": ["error", "as-needed"],

    // Keeps code maintainable & clear where we are importing from
    "import/no-relative-parent-imports": "error",
  },
  overrides: [
    {
      files: ["*.test.ts", "*.spec.ts"],
      rules: {
        /**
         * Disables explicit any for tests, this is useful to avoid
         * linter issues when inputting invalid params within tests
         */
        "@typescript-eslint/no-explicit-any": "off",
        "@typescript-eslint/no-unsafe-argument": "off",
      },
    },
  ],
};
