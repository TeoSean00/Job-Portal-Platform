import type {
  Department,
  RoleDetail,
  SkillDetail,
  StaffIdAPIResponse,
} from "@/types";

const mockAllSkills: SkillDetail[] = [
  {
    skill_status: "active",
    skill_id: 345678790,
    skill_name: "Typescript Developer",
  },
  { skill_status: "active", skill_id: 345678866, skill_name: "Java Developer" },
  {
    skill_status: "inactive",
    skill_id: 345678890,
    skill_name: "VMWare Villian",
  },
  {
    skill_status: "inactive",
    skill_id: 345678912,
    skill_name: "Pascal Programming",
  },
  {
    skill_status: "active",
    skill_id: 345678913,
    skill_name: "Python Programming",
  },
  {
    skill_status: "active",
    skill_id: 345678914,
    skill_name: "Certified Scrum Master",
  },
  { skill_status: "active", skill_id: 345678922, skill_name: "React Beast" },
  {
    skill_status: "active",
    skill_id: 345678927,
    skill_name: "LinkedIn Master",
  },
  { skill_status: "active", skill_id: 345678935, skill_name: "MongoDB Maniac" },
];

const mockDepartments: Department[] = [
  { value: "HR", label: "HR" },
  { value: "IT", label: "IT" },
  { value: "Sales", label: "Sales" },
  { value: "Finance", label: "Finance" },
];

const mockRoleDetails: RoleDetail[] = [
  {
    role_id: 234511581,
    role_name: "Fire Warden",
    role_description:
      "The Fire Warden is responsible for testing fire alarms and firefighting equipment and implementing risk assessment recommendations. In the event of a confirmed fire alarm or fire drill, the warden assists in the safe evacuation of staff and visitors from the premise immediately.",
    role_status: "active",
  },
  {
    role_id: 234567891,
    role_name: "Head, Talent Attraction",
    role_description:
      "The Head, Talent Attraction is responsible for strategic workforce planning to support the organisation's growth strategies through establishing talent sourcing strategies, determining the philosophy for the selection and securing of candidates and overseeing the onboarding and integration of new hires into the organisation. He/She develops various approaches to meet workforce requirements and designs employer branding strategies. He oversees the selection processes and collaborates with business stakeholders for the hiring of key leadership roles. As a department head, he is responsible for setting the direction and articulating goals and objectives for the team, and driving the integration of Skills Frameworks across the organisation's talent attraction plans.\nThe Head, Talent Attraction is an influential and inspiring leader who adopts a broad perspective in the decisions he makes. He is articulate and displays a genuine passion for motivating and developing his team.",
    role_status: "inactive",
  },
  {
    role_id: 234567893,
    role_name: "Agile Coach (SM)",
    role_description:
      "The Agile Coach (SM) coaches teams in the conduct of Agile practices and the implementation of Agile methodologies and practices in the organisation and acts as an effective Scrum Master in Agile Scrum teams.",
    role_status: "active",
  },
  {
    role_id: 234567899,
    role_name: "Butcher",
    role_description: "added by elton on 22/9/23 10.12pm to fix fk constraints",
    role_status: "active",
  },
];

const mockManager: StaffIdAPIResponse = {
  staff_id: 123456787,
  fname: "FAUD",
  lname: "NIZAM",
  dept: "SALES",
  email: "faud_nizam@all-in-one.com.sg",
  phone: "60-03-21345678",
  biz_address:
    "Unit 3A-07, Tower A, The Vertical Business Suite, 8, Jalan Kerinchi, Bangsar South, 59200 Kuala Lumpur, Malaysia",
  sys_role: "manager",
};

export { mockAllSkills, mockDepartments, mockRoleDetails, mockManager };
