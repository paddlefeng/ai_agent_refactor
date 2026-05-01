from agents.planner import PlannerAgent
from agents.analyzer import AnalyzerAgent
from agents.refactor import RefactorAgent
from agents.tester import TesterAgent
from agents.reporter import ReporterAgent

class AgentSystem:
    def __init__(self):
        self.planner = PlannerAgent()
        self.analyzer = AnalyzerAgent()
        self.refactor = RefactorAgent()
        self.tester = TesterAgent()
        self.reporter = ReporterAgent()

    def run(self, file_path):
        print("🚀 启动 Agent 系统...\n")

        plan = self.planner.plan(file_path)

        issues = self.analyzer.analyze(file_path)

        suggestions = self.refactor.refactor(issues)

        test_result = self.tester.test()

        report = self.reporter.generate(
            file_path, issues, suggestions, test_result
        )

        return report


if __name__ == "__main__":
    system = AgentSystem()
    result = system.run("sample_code.py")

    print(result)