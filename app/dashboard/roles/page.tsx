
import { RoleTable } from "@/components/RoleTable";

const RolesPage = () => {
  const roleData = [
    {
      roleId: 1,
      roleName: "Temp Role 1",
      roleDescription: "This is a temporary role 1",
      roleStatus: "active",
    },
    {
      roleId: 2,
      roleName: "Temp Role 2",
      roleDescription: "This is a temporary long description 2 This is a temporary long description 2 This is a temporary long description 2 This is a temporary long description 2 This is a temporary long description 2",
      roleStatus: "active",
    },
    {
      roleId: 3,
      roleName: "Temp Inactive Role",
      roleDescription: "This is a temporary inactive role",
      roleStatus: "inactive",
    },
  ];

  return (
    <>
      <div className="">Roles
        <RoleTable roleData={roleData} />
      </div>
    </>
  )
};

export default RolesPage;
