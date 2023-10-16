import RoleListing from "@/components/role-page/role-page";

interface PageProps {
  params: { roleid: number };
}
export interface PageData {
  roleid: number;
  roleName: string;
  roleDescription: string;
  skillsRequired: string[];
}

const rolePage = (props: PageProps) => {
  const data: PageData = {
    roleid: props.params.roleid,
    roleName: "Software Engineer",
    roleDescription: "Software Engineer",
    skillsRequired: ["Python", "React", "Javascript", "Java", "C++", "C#"],
  };
  return (
    <>
      <RoleListing data={data} />
    </>
  );
};
export default rolePage;
