declare type SidebarNavItem = {
  title: string;
  href: string;
  icon: React.ReactElement;
};

declare type Skill = { value: string; label: string };
declare type Department = { value: string; label: string };

declare type RoleFormProps = {
  skillList: Skill[];
  departments: Department[];
};

declare type RoleFormValues = z.infer<typeof roleFormSchema>;
