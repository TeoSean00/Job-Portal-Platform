interface PageProps {
  params: { roleid: number };
}

const rolePage = (props: PageProps) => (
  <>
    <div>rolePage {props.params.roleid}</div>
  </>
);

export default rolePage;
