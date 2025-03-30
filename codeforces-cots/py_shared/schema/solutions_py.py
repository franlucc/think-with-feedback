import pydantic


class SolutionsRow(pydantic.BaseModel):
    idx: int

    inputs: 'SolutionsInputs'

    response_len: int

    think_code_blocks: list[str]
    answer_candidates: list[str]
    final_answer: str | None

    # TODO group these?
    has_input: bool
    has_stdin: bool
    has_strange_stdin: bool
    has_print: bool
    has_extra_backticks_in_thinks: bool
    has_extra_midparagraph_backticks_in_thinks: bool


class SolutionsInputs(pydantic.BaseModel):
    prompt: str
    response: str

    title: str
    contest_name: str
    contest_start_year: int
    examples: list[dict]


def make_rendered(row: SolutionsRow, out):
    print("# {title} ({contest_name}, {contest_start_year})".format(**row.inputs.__dict__), file=out)
    print("# Prompt", file=out)
    print(row.inputs.prompt, file=out)
    print("# Response", file=out)
    print(row.inputs.response, file=out)
    print("\n# Think code blocks", file=out)
    not_first = False
    for ans in row.think_code_blocks:
        if not_first:
            print('\n---\n', file=out)
        print('```python', file=out)
        print(ans, file=out)
        print('```', file=out)
        not_first = True
