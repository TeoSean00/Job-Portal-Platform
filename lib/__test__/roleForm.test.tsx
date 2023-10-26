import { render, screen } from "@testing-library/react";
import React from "react";

import RoleForm from "@/components/create-role/RoleForm";
import {
  mockAllSkills,
  mockDepartments,
  mockRoleDetails,
} from "@/lib/__test__/mocks/mockInputs";

jest.mock("@clerk/nextjs", () => ({
  useSession: () => ({
    session: {
      user: {
        id: "test-id",
        publicMetadata: {
          role: "test-role",
        },
      },
    },
  }),
}));

describe("<RoleForm />", () => {
  test("renders input fields, comboboxes, etc.", () => {
    // We'll provide some mock data to the component for the test
    const mockData = {
      departments: mockDepartments,
      roles: mockRoleDetails,
      allSkills: mockAllSkills,
    };

    render(<RoleForm {...mockData} />);

    expect(screen.getByText("Role")).toBeVisible();
    expect(screen.getByText("Listing Id")).toBeVisible();
    expect(screen.getByText("Listing Description")).toBeVisible();
    expect(screen.getByText("Listing Id")).toBeVisible();
    expect(screen.getByText("Role's Manager")).toBeVisible();
  });

  test("matches snapshot", () => {
    const mockData = {
      departments: mockDepartments,
      roles: mockRoleDetails,
      allSkills: mockAllSkills,
    };

    const { asFragment } = render(<RoleForm {...mockData} />);
    expect(asFragment()).toMatchSnapshot();
  });
});
