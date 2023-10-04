import { render, screen } from "@testing-library/react";
import React from "react";

import "@testing-library/jest-dom/extend-expect"; // for the "toBeInTheDocument" matcher
import RoleForm from "./RoleForm"; // adjust the import to your file structure

// Mock data to be passed as props to the RoleForm component
const mockSkillList = [
  { id: "1", name: "JavaScript" },
  { id: "2", name: "TypeScript" },
];
const mockDepartments = [
  { id: "1", name: "Engineering" },
  { id: "2", name: "Marketing" },
];

describe("<RoleForm />", () => {
  test("it renders without crashing", () => {
    render(
      <RoleForm departments={mockDepartments} skillList={mockSkillList} />,
    );
    const submitButton = screen.getByRole("button", { name: /create role/i });
    expect(submitButton).toBeInTheDocument();
  });
});
