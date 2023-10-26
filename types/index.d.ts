import { decl } from "postcss";

declare type SidebarNavItem = {
  title: string;
  href: string;
  icon: React.ReactElement;
};

declare type User = {
  staff_id: number;
  fname: string;
  lname: string;
  dept: string;
  email: string;
  phone: string;
  biz_address: string;
  sys_role: string;
};

declare type Skill = { value: string; label: string };

declare type Department = { value: string; label: string };

declare type RoleDetail = {
  role_id: number;
  role_name: string;
  role_description: string;
  role_status: string;
};

declare type SkillDetail = {
  skill_status: string;
  skill_name: string;
  skill_id: number;
};

declare type RoleSkillId = {
  role_id: number;
  skill_id: number;
};

declare type SkillAPIResponse = {
  skill_status: string;
  skill_name: string;
  skill_id: number;
};

declare type RoleFormProps = {
  departments: Department[];
  roles: RoleDetail[];
  allSkills: SkillAPIResponse[];
};
// declare type RoleFormValues = z.infer<typeof roleFormSchema>;

declare type RoleFormValues = {
  roleName: string;
  roleDescription: string;
  departments: string;
  skills: { value: string }[];
  dateRange: {
    from: Date;
    to: Date;
  };
};

declare type RoleSkill = {
  skill_id: number;
  skill_name: string;
  skill_status: string;
};

declare type RoleItem = {
  role_id: number;
  role_name: string;
  role_desc: string;
  role_status: string;
  skills: RoleSkill[];
};
