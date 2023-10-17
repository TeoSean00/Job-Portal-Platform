declare type SidebarNavItem = {
  title: string;
  href: string;
  icon: React.ReactElement;
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
declare type RoleFormValues = z.infer<typeof roleFormSchema>;
