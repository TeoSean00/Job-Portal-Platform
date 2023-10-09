import { render } from "@testing-library/react";
import React from "react";

// import "@testing-library/jest-dom/extend-expect";
import RoleForm from "../../components/create-role/RoleForm";

const mockSkillList = [
  { value: "Pascal Programming", label: "Pascal Programming" },
  { value: "Python Programming", label: "Python Programming" },
  { value: "Certified Scrum Master", label: "Certified Scrum Master" },
  { value: "Marketing", label: "Marketing" },
  { value: "Scrum", label: "Scrum" },
  { value: "UI/UX", label: "UI/UX" },
  { value: "Product Management", label: "Product Management" },
];

const mockDepartments = ["HR", "IT", "Sales", "Finance"].map((department) => ({
  value: department,
  label: department,
}));

describe("<RoleForm />", () => {
  it("should match snapshot", () => {
    const { asFragment } = render(
      <RoleForm departments={mockDepartments} skillList={mockSkillList} />,
    );
    expect(asFragment()).toMatchSnapshot();
  });
});
