import { DataTable } from "@/components/data-table/DataTable";
import { Payment, columns } from "@/components/ui/";

const RolesPage = () => {
  const tempSkills = [
    { label: "Skill 1", value: "skill 1" },
    { label: "Skill 2", value: "skill 2" },
    { label: "Skill 3", value: "skill 3" },
    { label: "Skill 4", value: "skill 4" },
  ];
  const data = [
    {
      roleId: 1,
      roleName: "Temp Role 1",
      roleDescription: "This is a temporary role 1",
      roleStatus: "active",
      skillRequired: ["skill 1", "skill 2"],
    },
    {
      roleId: 2,
      roleName: "Temp Role 2",
      roleDescription:
        "This is a temporary long description 2 This is a temporary long description 2 This is a temporary long description 2 This is a temporary long description 2 This is a temporary long description 2",
      roleStatus: "active",
      skillRequired: ["skill 2", "skill 3"],
    },
    {
      roleId: 3,
      roleName: "Temp Inactive Role",
      roleDescription: "This is a temporary inactive role",
      roleStatus: "inactive",
      skillRequired: ["skill 3", "skill 4"],
    },
  ];

  return (
    <>
      <div className="">
        Roles
        <DataTable
          columns={columns}
          data={data}
          filterableColumns={[
            {
              id: "skillRequired",
              title: "Required Skills",
              options: tempSkills,
            },
          ]}
          searchableColumns={[
            {
              id: "roleName",
              title: "Role Name",
            },
          ]}
        />
      </div>
    </>
  );
};

export default RolesPage;
