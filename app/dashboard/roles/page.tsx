import { Payment, columns } from "@/components/ui/Colums";
import { DataTable } from "@/components/data-table/DataTable";

const RolesPage = () => {
  // const data = [
  //   {
  //     id: "728ed52f",
  //     amount: 100,
  //     status: "pending",
  //     email: "m@example.com",
  //   },
  // ];
  const data = [
    {
      roleId: 1,
      roleName: "Temp Role 1",
      roleDescription: "This is a temporary role 1",
      roleStatus: "active",
      skillRequired : ["skill 1", "skill 2"]
    },
    {
      roleId: 2,
      roleName: "Temp Role 2",
      roleDescription:
        "This is a temporary long description 2 This is a temporary long description 2 This is a temporary long description 2 This is a temporary long description 2 This is a temporary long description 2",
      roleStatus: "active",
      skillRequired : ["skill 2", "skill 3"]
    },
    {
      roleId: 3,
      roleName: "Temp Inactive Role",
      roleDescription: "This is a temporary inactive role",
      roleStatus: "inactive",
      skillRequired : ["skill 3", "skill 4"]
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
              options: ["skill 1"],
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
